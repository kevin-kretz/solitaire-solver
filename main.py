import random, os
from Card import Card

def build_columns():
    for index, column in enumerate(columns):
        while len(column) <= index:
            column.append(deck.pop())
        column[-1].face_up = True

def build_deck():
    for suit in suits:
        for symbol in symbols:
            card = Card(suit, symbol)
            deck.append(card)

def can_move_to_foundation(card:Card):
    for foundation in foundations:
        if len(foundation) == 0:
            if card.value == 1:
                return True
        elif len(foundation) >= 1:
            if card.suit == foundation[-1].suit and card.value == foundation[-1].value + 1:
                return True
    return False

def cards_alternate_colors(column_index:int, number_of_cards:int):
    previous_card = None
    card_index = -number_of_cards

    while card_index < 0 :
        if previous_card != None and is_opposite_color(previous_card, columns[column_index][card_index]):
            return False
        card_index += 1
    
    return True

def flip_card():
    if len(deck) == 0:
        reset_deck()

    waste.append(deck.pop())
    waste[-1].face_up = True

def foundations_are_empty():
    for foundation in foundations:
        if len(foundation) > 0:
            return False
    
    return True

def game_over():
    for foundation in foundations:
        if len(foundation) < 13:
            return False
    return True
    
def get_column_index(cards:list[Card]):
    index = input("Which column would you like to place the card(s)? (Enter -1 to cancel move.) ")

    if not index.isdigit():
        print("Expected number between 0 - 6.")
        return None
    
    index = int(index)

    if index == -1 or not is_valid_column_index(cards, index):
        return None

    return index
    
def get_destination(cards:list[Card]):
    destination = input(f"\nWhere would you like to place the card(s)? ('c' = columns, 'f' = foundations, 'z' = cancel move) ")
    
    if destination == "z" or not is_valid_destination(cards, destination):
        return None

    return destination

def get_face_up_cards_in_column(index:int):
    number_of_face_up_cards = 0

    for card in columns[index]:
        if card.face_up:
            number_of_face_up_cards += 1
    
    return number_of_face_up_cards

def get_foundation_index(card:Card):
    for index, foundation in enumerate(foundations):
        if len(foundation) == 0:
            if card.value == 1:
                return index
        elif len(foundation) >= 1:
            if card.suit == foundation[-1].suit and card.value == foundation[-1].value + 1:
                return index

def get_number_of_cards(index:int):
    if get_face_up_cards_in_column(index) == 1:
        return 1
    
    number_of_cards = input("How many cards would you like to grab? (Enter 0 to cancel move.) ")
    if number_of_cards.isdigit():
        number_of_cards = int(number_of_cards)
    else:
        print("Expected number. Try again.")
        return None

    if number_of_cards == 0 or not is_valid_number_of_cards(index, number_of_cards):
        return None
    
    return number_of_cards
    
def get_source():
    source = input(f"\nWhere would you like to grab from? ('c' = columns, 'd' = deck, 'w' = waste, 'f' = foundations) ")
    
    if not is_valid_source(source):
        return None
    
    return source

def get_source_index(source:str):
    index = input("Which column would you like to grab from? (Enter -1 to cancel move.) ")

    if not index.isdigit():
        print("Expected digit. Try again.")
        return None
    
    index = int(index)

    if index == -1 or not is_valid_source_index(source, index):
        return None

    return index

def handle_move():
    source = get_source()

    if source == "d":
        flip_card()
        return None
        
    elif source == "c":
        source_index = get_source_index(source)
        
        if source_index == None:
            return None
        
        number_of_cards = get_number_of_cards(source_index)

        if number_of_cards == None:
            return None
        
        else:
            cards_to_check = columns[source_index][-number_of_cards:]

    elif source == "f":
        source_index = get_source_index(source)
        number_of_cards = 1
        
        if source_index == None:
            return None
        
        else:
            cards_to_check = foundations[source_index][-1:]
    
    elif source == "w":
        source_index = -1
        number_of_cards = 1
        cards_to_check = waste[-1:]

    else:
        print("Check get_source()")
        return None
        
    destination = get_destination(cards_to_check)
    
    if destination == None:
        return None
    
    elif destination == "c":
        destination_index = get_column_index(cards_to_check)
        
        if destination_index == None:
            return None
    
    elif destination== "f":
        if source == "c":
            destination_index = get_foundation_index(columns[source_index][-1])
        elif source == "f":
            destination_index = get_foundation_index(foundations[source_index][-1])
        elif source == "w":
            destination_index = get_foundation_index(waste[-1])
        else:
            print("Unexpected source. Can't move to foundation.")

    else:
        print("Check get_destination()")

    if number_of_cards == 1:
        move_card(source, destination, source_index, destination_index)
    elif number_of_cards > 1:
        move_cards(source_index, destination_index, number_of_cards)
    else:
        print("Check get_number_of_cards()")

def is_opposite_color(card1:Card, card2:Card):
    return card1.color != card2.color

def is_valid_column_index(cards:list[Card], index:int):
    if index < 0 or index > 6:
        print("Expected index between 0-6. Try again.")
        return False
    
    if len(columns[index]) == 0:
        if cards[0].value != 13:
            print("You can only place Kings on an empty column. Try again.")
            return False
        else:
            return True
    elif not is_opposite_color(cards[0], columns[index][-1]):
        print("The cards are not opposite colors. Try again.")
        return False
    
    elif cards[0].value != columns[index][-1].value - 1:
        print("The highest card from the source needs to be 1 lower than the destination.")
        return False
    
    return True

def is_valid_destination(cards: list[Card], destination:str):
    if destination != "c" and destination != "f":
        print("You can only choose 'c' of 'f'. (Enter 'z' to cancel the move) ")
        return False

    if destination == "f":
        if len(cards) > 1:
            print("You can only move 1 to the foundation at a time. Try again.")
            return False
        elif not can_move_to_foundation(cards[0]):
            print("This card can't go on the foundation. Choose a column instead.")
            return False
    
    return True

def is_valid_number_of_cards(column_index:int, number_of_cards:int):
    if number_of_cards <= 0:
        print("Number of cards should be a positive number. Try again.")
        return False
    elif number_of_cards > get_face_up_cards_in_column(column_index):
        print("There aren't that many face up cards in the column. Try again.")
        return False
    elif not cards_alternate_colors(column_index, number_of_cards):
        print("Not all the cards alternate color. Try again.")
        return False
    return True
    
def is_valid_source(source:str):
    if source != "c" and source != "d" and source != "w" and source != "f":
        print("Not a valid source. Try again.")
        return False
        
    elif source == "f" and foundations_are_empty():
        print("There are no cards in the foundation. Try another source.")
        return False
    
    else:
        return True
    
def is_valid_source_index(source:str, index:int):
    if source == "c":
        if index < 0 or index > 6:
            print("Index is out of range. Pick a number 0-6.")
            return False
        elif len(columns[index]) <= 0:
            print("There are no cards in that column. Try again.")
            return False
    elif source == "f":
        if index < 0 or index > 3:
            print("Index is out of range. Pick a number 0-3.")
            return False
        elif len(foundations[index]) <= 0:
            print("There are no cards in that foundation. Try again.")
            return False
    return True

def move_card(source:str, destination:str, source_index:int = None, destination_index:int = None):
    if source == "c":
        if destination == "c":
            columns[destination_index].append(columns[source_index].pop())
        elif destination == "f":
            foundations[destination_index].append(columns[source_index].pop())
        
        if len(columns[source_index]) >= 1:
            columns[source_index][-1].face_up = True

    elif source == "f":
        if destination == "c":
            columns[destination_index].append(foundations[source_index].pop())
        elif destination == "f":
            foundations[destination_index].append(foundations[source_index].pop())
    
    elif source == "w":
        if destination == "c":
            columns[destination_index].append(waste.pop())
        elif destination == "f":
            foundations[destination_index].append(waste.pop())

def move_cards(source_index:int, destination_index:int, number_of_cards:int):
    cards = []
    card_counter = number_of_cards

    while card_counter > 0:
        cards.append(columns[source_index].pop())
        card_counter -= 1
    while len(cards) > 0:
        columns[destination_index].append(cards.pop())

    if len(columns[source_index]) >= 1:
        columns[source_index][-1].face_up = True

def print_board():
    print_top_row()
    print(f"\n")   
    print_columns()

def print_columns():
    longest_column_length = 0
    for column in columns:
        if len(column) > longest_column_length:
            longest_column_length = len(column)
    
    for i in range(longest_column_length):
        for j, column in enumerate(columns):
            if i == 0 and len(column) == 0:
                print("[     ]", end=" ")
            elif i < len(column):
                print(columns[j][i], end=" ")
            else:
                print("       ", end=" ")
        print("")

def print_deck():
    if len(deck) >= 1:
        print(f"[  ?  ]", end=" ")
    else:
        print("       ", end=" ")

def print_foundations():
    for column in foundations:
        if len(column) >= 1:
            print(column[-1], end=" ")
        else:
            print("[     ]", end=" ")

def print_top_row():
    print_deck()
    print_waste()
    print("       ", end=" ")
    print_foundations()

def print_waste():
    if len(waste) >= 1:
        print(waste[-1], end=" ")
    else:
        print("[     ]", end=" ")

def reset_deck():
    while len(waste) > 0:
        deck.append(waste.pop())


deck = []
suits = ["♥", "♦", "♣", "♠"]
symbols = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", ]

columns = [[],[],[],[],[],[],[]] # Columns of cards on game "board"
foundations = [[],[],[],[]] # Cards solved from columns
waste = [] # Cards flipped from deck

build_deck()
random.shuffle(deck)
build_columns()
flip_card()

os.system("clear")

while not game_over():
    print_board()
    handle_move()
    os.system("clear")

print(f"You did it! Great job!\n")
print_board()