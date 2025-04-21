class House():
    def __init__(self):
        self.board = [0, 0, 0, 0, 0]
        self.readBoard = [0, 0, 0, 0, 0]

    def board(self, board):
        self.board = board
        for i in self.board:
            self.readBoard = self.board[i].replace(" 1 ", " Ace ").replace(" 11 ", " Jack ").replace(" 12 ", " Queen ").replace(" 13 ", " King ").replace("S", "of Spades").replace("H", "of Hearts").replace("D", "of Diamonds").replace("C", "of Clubs")[1:]
        
    def communityCards(self):
        for i in range(3):
            print(self.readBoard[i])

    def flop(self):
        pass

    def turn(self):
        pass

    def river(self):
        pass