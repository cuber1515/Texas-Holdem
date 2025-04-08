class Player():
    def __init__(self):
        self.hand = []
        self.money = 1000

    def newDeal(self, hand):
        self.hand = hand