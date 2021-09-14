import numpy as np

from PieceFactory import create_pawn


class Board:
    def __init__(self):
        self.tiles = []
        for y in range(8):
            self.tiles.append([])
            for x in range(8):
                self.tiles[y].append(None)
        self.current = ""

    def get_piece(self, x, y):
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return self.tiles[x][y]

    def setPieces(self):
        for i in range(8):
            self.tiles[i][1] = create_pawn(i, 1, 1)
            self.tiles[i][6] = create_pawn(i, 6, -1)


    def print(self):
        for y in range(8):
            output = ""
            for x in range(8):
                if self.tiles[x][7-y] is not None:
                    output += str(self.tiles[x][7-y].id) + "  "
                else:
                    output += "_" + "  "

            print(output)

    def get_all_moves(self, is_white):
        moves = []
        for y in range(8):
            for x in range(8):
                if self.tiles[x][y] is not None and self.tiles[x][y].is_white == is_white:
                    new_moves = self.tiles[x][y].get_legal_tiles(self)
                    for new_x, new_y, result in new_moves:
                        moves.append((x, y, new_x, new_y, result))

        return moves

    def move(self, x, y, x2, y2, taken_piece):
        piece = self.get_piece(x, y)
        if piece:
            if taken_piece is not True and taken_piece is not False:
                self.tiles[taken_piece.x][taken_piece.y] = None
            piece.move()
            self.tiles[x][y] = None
            self.tiles[x2][y2] = piece
            piece.x = x2
            piece.y = y2
        else:
            print('there is no piece')

