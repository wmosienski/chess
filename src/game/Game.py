import random


class Game:
    def __init__(self, model):
        self.model = model
        self.restart()

    def restart(self):
        self.is_white = True
        self.model.board.restart()

    def make_random_move(self):
        board = self.model.board
        moves = board.get_all_moves(self.is_white)
        x, y, x2, y2, result = moves[random.randint(0, len(moves) - 1)]
        print("making move: ")
        print(x, y, x2, y2, result)
        board.move(x, y, x2, y2, result)
        self.is_white = not self.is_white

    def make_move(self, x, y, x2, y2):
        pass
