import random

class Card:
    def __init__(self, suit, symbol):
        self.suit = suit
        self.symbol = symbol
        self.face_up = False

        if self.suit == "♥" or self.suit == "♦":
            self.color = "red"
        else:
            self.color = "black"
        
        if self.symbol == "K" or self.symbol == "Q" or self.symbol == "J" or self.symbol == "A":
            if self.symbol == "K":
                self.value = 13
            elif self.symbol == "Q":
                self.value = 12
            elif self.symbol == "J":
                self.value = 11
            else:  # If ace
                self.value = 1

        else:
            self.value = int(self.symbol)

    def __str__(self):
        if self.face_up:
            if self.value == 10:
                return str(f"[{self.symbol} {self.suit} ]")
            else:
                return str(f"[ {self.symbol} {self.suit} ]")
        else:
            return "[  ?  ]"
    
    def debug_string(self):
        return str(f"{self.symbol}{self.suit} face_up={self.face_up}")

def build_deck():
    for suit in suits:
        for symbol in symbols:
            card = Card(suit, symbol)
            deck.append(card)

def game_over():
    pass

def get_card_from_deck():
    card = deck[0]
    deck.pop(0)
    return card

def build_columns():
    number_of_cards_to_place = 1

    for index, column in enumerate(columns):
        while len(column) < index + 1:
            card = get_card_from_deck()
            if len(column) == index:
                card.face_up = True
            column.append(card)

def print_columns():
    for i in range(7):
        for column in columns:
            if i+1 <= len(column):
                print(column[i], end=" ")
            else:
                print("       ", end=" ")
        print("")

def print_deck():
    if len(deck) >= 1:
        print(f"[  ?  ]", end=" ")
    else:
        print("     ", end=" ")

def print_cascade():
    if len(cascade) >= 1:
        print(cascade[-1], end=" ")
    else:
        print("     ", end=" ")

def print_foundations():
    for column in foundations:
        if len(column) >= 1:
            print(column[-1], end=" ")
        else:
            print("[     ]", end=" ")

def print_top_row():
    print_deck()
    print_cascade()
    print("       ", end=" ")
    print_foundations()

def print_board():
    print_top_row()
    print("")
    print("")     
    print_columns()

def flip_card():
    card = get_card_from_deck()
    card.face_up = True
    cascade.append(card)

deck = []
suits = ["♥", "♦", "♣", "♠"]
symbols = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", ]

columns = [[],[],[],[],[],[],[]] # Columns of cards on game "board"
foundations = [[],[],[],[]] # Cards solved from columns
cascade = [] # Cards flipped from deck

build_deck()
random.shuffle(deck)
build_columns()
flip_card()
print_board()