from colorama import Fore, Back, Style, init

class Card:
    def __init__(self, rank, suit):
        init()
        self.rank = rank
        self.suit = suit
        self.value = self.get_value()  
        self.color = self.get_color()

    def __str__(self):
        return f"{self.get_color()}{self.suit}{self.rank}{Style.RESET_ALL}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def get_value(self):
        if self.rank == 'A':
            return 14
        elif self.rank == 'K':
            return 13
        elif self.rank == 'Q':
            return 12
        elif self.rank == 'J':
            return 11
        else:
            return int(self.rank)
        
    def get_color(self):
        if (self.suit == '\u2665' or self.suit == '\u2666'):
            return Fore.RED + Back.BLACK
        else:
            return Fore.BLACK + Back.WHITE
        
        