from cards import Cards
from player import Player
from house import House

deck = Cards()
player1 = Player()
house = House()

deck.shuffle()

player1.newDeal([deck.deal(), deck.deal()])

board = deck.board()

house.communityCards()