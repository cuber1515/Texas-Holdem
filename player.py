class Player():
    def __init__(self):
        self.hand = []
        self.money = 1000

    def newDeal(self, hand):
        self.hand = hand
    
    def printHand(self):
        card1 = self.hand[0].replace(" 1 ", " Ace ").replace(" 11 ", " Jack ").replace(" 12 ", " Queen ").replace(" 13 ", " King ").replace("S", "of Spades").replace("H", "of Hearts").replace("D", "of Diamonds").replace("C", "of Clubs")
        card2 = self.hand[1].replace(" 1 ", " Ace ").replace(" 11 ", " Jack ").replace(" 12 ", " Queen ").replace(" 13 ", " King ").replace("S", "of Spades").replace("H", "of Hearts").replace("D", "of Diamonds").replace("C", "of Clubs")
        print(f"Your hand is{card1} and{card2}")
