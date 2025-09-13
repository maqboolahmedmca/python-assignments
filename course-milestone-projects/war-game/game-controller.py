from colorama import Fore, Style, init
import time
from deck import Deck
from player import Player

class GameController:
    def __init__(self):
        init()
        self.deck = Deck()
        self.players = []
        self.game_over = False
        
    def add_player(self, player):
        self.players.append(player)

    def distribute_cards(self):
        for index, card in enumerate(self.deck.cards):
            self.players[index % 2].hand.append(card)
        
        print("_" * 100)    
        # self.players[0].hand.sort()
        self.players[0].show_cards()
        print("_" * 100)  
        # self.players[1].hand.sort()
        self.players[1].show_cards()
        print("_" * 100)  


    def deal_cards(self):
        for player in self.players:
            player.hand.append(self.deck.draw_card())
            
    def play_game(self):
        cards = []
        while not self.check_game_over():
            p1card = player1.play_card()
            p2card = player2.play_card()
            print(f"{player1} played {p1card} | {player2} played {p2card}")

            if (p1card.__eq__(p2card)):
                cards.extend([p1card, p2card])
            elif (p1card > p2card):
                player1.hand.append(p2card)
                if (len(cards) > 0):
                    player1.hand.extend(cards)
                print(f"{', '.join([str(p1card)] + [str(c) for c in cards])} added in {player1}'s deck")
                cards = []
            else:
                player2.hand.append(p1card)
                if (len(cards) > 0):
                    player2.hand.extend(cards)
                print(f"{', '.join([str(p2card)] + [str(c) for c in cards])} added in {player2}'s deck")
                cards = []

            time.sleep(SLEEP_TIME)
                
    def check_game_over(self):
        if len(player1.hand) == 0:
            return True
        if len(player2.hand) == 0:   
            return True      
        return False
        
SLEEP_TIME = 100 / 1000

game = GameController()
player1 = Player("Fred")
player2 = Player("Joe")
game.add_player(player1)
game.add_player(player2)

game.distribute_cards()
game.play_game()

print()
print(Fore.GREEN + "*" * 25)   
if len(player1.hand) == 0: 
    print(f"{Fore.GREEN}* {player2} WON the game *{Style.RESET_ALL}")
elif len(player2.hand) == 0:   
    print(f"{Fore.GREEN}* {player1} WON the game *{Style.RESET_ALL}") 
print(Fore.GREEN + "*" * 25) 