from enum import IntEnum

class Suit(IntEnum):
    HEARTS = 0
    CLUBS = 1
    SPADES = 2
    DIAMONDS = 3

class CardValue(IntEnum):
    TWO = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    ACE = 12

class Card:

    def __init__(self, suit : Suit, value : CardValue, hidden : bool = False):
        self.suit = suit
        self.value = value
        self.hidden = hidden

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value
        
    def getCardStr(self):
        #ASCII Card Designs from: https://www.asciiart.eu/miscellaneous/playing-cards

        if not self.hidden:
            __hearts_str   = (" _ _ ", "( v )", " \\ / ", "  v  ")
            __clubs_str    = ("  _  ", " ( ) ", "( ' )", "  |  ")
            __spades_str   = ("  .  ", " /.\\ ", "(_._)", "  |  ")
            __diamonds_str = ("  .  ", " / \\ ", " \\ / ", "  V  ")

            __suits_str = (__hearts_str, __clubs_str, __spades_str, __diamonds_str)
            __val_str   = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

            card  = [f" _______ "]
            card += [f"|{__val_str[self.value]:<2s}     |"]
            card += [f"| {__suits_str[self.suit][0]} |"]
            card += [f"| {__suits_str[self.suit][1]} |"]
            card += [f"| {__suits_str[self.suit][2]} |"]
            card += [f"| {__suits_str[self.suit][3]} |"]
            card += [f"|       |"]
            card += [f"|_____{__val_str[self.value]:_>2s}|"]

            return card
        else:

            card  = [f" _______ "]
            card += [f"|       |"]
            card += [f"| /\/\/ |"]
            card += [f"| \/\/\ |"]
            card += [f"| ~~~~~ |"]
            card += [f"| \/\/\ |"]
            card += [f"| /\/\/ |"]
            card += [f"|_______|"]
            
            return card