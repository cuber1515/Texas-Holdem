from cards import Cards
from player import Player

deck = Cards()
player1 = Player()

deck.shuffle()

player1.newDeal([deck.deal(), deck.deal()])

print(player1.hand)