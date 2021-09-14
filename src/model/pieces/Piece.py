from src.utils.utils import rem_dup


class Piece:
    def __init__(self, id, x, y, direction):
        if direction == 1:
            self.is_white = True
        else:
            self.is_white = False
        self.direction = direction
        self.id = id
        self.x = x
        self.y = y
        self.has_moved = False
        self.has_just_moved = False
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)

    def get_legal_tiles(self, board):
        tiles = []
        for move in self.moves:
            tiles += move.get_possible_tiles(board, self)

        return rem_dup(tiles)

    def move(self):
        self.has_moved = True
        self.has_just_moved = True
