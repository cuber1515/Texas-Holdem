from random import shuffle

class Cards():
    def __init__(self):
        self.deck = []
        for i in range (13):
            self.deck.append(f" {i + 1} S")
            self.deck.append(f" {i + 1} H")
            self.deck.append(f" {i + 1} D")
            self.deck.append(f" {i + 1} C")

        self.topCard = 0

        # return self.deck
    
    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        if self.topCard == 51:
            print("no more cards")
            self.shuffle()
            self.topCard = 0
        else:
            self.topCard += 1
        
        return self.deck[self.topCard]