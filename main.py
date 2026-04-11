import random

class Card:
    def __init__(self, suit, symbol):
        self.suit = suit
        self.symbol = symbol
        self.face_up = True

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
            return str(f"[{self.symbol} {self.suit}]")
        else:
            return "[?]"
    
    def debug_string(self):
        return str(f"{self.symbol}{self.suit} face_up={self.face_up}")

def build_deck():
    for suit in suits:
        for symbol in symbols:
            card = Card(suit, symbol)
            deck.append(card)

def game_over():
    pass

def place_card():
    card = deck[0]
    deck.pop(card)
    return card
    

deck = []
suits = ["♥", "♦", "♣", "♠"]
symbols = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", ]

columns = [[],[],[],[],[],[],[]] # Columns of cards on game "board"
foundations = [[],[],[],[]] # Cards solved from columns
cascade = [] # Cards flipped from deck

build_deck()
random.shuffle(deck)

print(deck[0])