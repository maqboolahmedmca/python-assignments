import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['\u2665', '\u2666', '\u2663', '\u2660']:
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.cards)
    
    #
    def draw_card(self):    
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)
