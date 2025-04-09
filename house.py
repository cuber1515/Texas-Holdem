class House():
    def __init__(self):
        self.board = []

    def board(self, board):
        self.board = board
        
    def communityCards(self, board):
        for i in range(3):
            bluh = board[i].replace(" 1 ", " Ace ").replace(" 11 ", " Jack ").replace(" 12 ", " Queen ").replace(" 13 ", " King ").replace("S", "of Spades").replace("H", "of Hearts").replace("D", "of Diamonds").replace("C", "of Clubs")[1:]
            print(bluh)

    def flop(self):
        pass

    def turn(self):
        pass

    def river(self):
        pass