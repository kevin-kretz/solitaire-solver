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