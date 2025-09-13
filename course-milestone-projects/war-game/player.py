import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return self.__str__()
    
    def show_cards(self):
        print(f"{self.name} cards:")
        print(','.join([str(card) for card in self.hand]))

    def play_card(self):
        size = len(self.hand)
        if (size > 0):
            pick = random.randint(0, size - 1)
            card = self.hand.pop(pick)
            return card
        return None

            
    