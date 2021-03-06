from src.model.pieces.PieceFactory import create_pawn, create_rook, create_bishop


class Board:
    def __init__(self):
        self.tiles = []
        self.restart()

    def restart(self):
        self.clear()
        self.setPieces()

    def get_piece(self, x, y):
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return self.tiles[x][y]

    def clear(self):
        self.tiles = []
        for y in range(8):
            self.tiles.append([])
            for x in range(8):
                self.tiles[y].append(None)

    def setPieces(self):
        for i in range(8):
            self.tiles[i][1] = create_pawn(i, 1, 1)
            self.tiles[i][6] = create_pawn(i, 6, -1)

        self.tiles[0][0] = create_rook(0, 0, 1)
        self.tiles[7][0] = create_rook(7, 0, 1)
        self.tiles[0][7] = create_rook(0, 7, -1)
        self.tiles[7][7] = create_rook(7, 7, -1)

        self.tiles[2][0] = create_bishop(2, 0, 1)
        self.tiles[2][7] = create_bishop(2, 7, -1)
        self.tiles[5][0] = create_bishop(5, 0, 1)
        self.tiles[5][7] = create_bishop(5, 7, -1)

    def get_all_moves(self, is_white):
        moves = []
        for y in range(8):
            for x in range(8):
                if self.tiles[x][y] is not None and self.tiles[x][y].is_white == is_white:
                    new_moves = self.tiles[x][y].get_legal_tiles(self)
                    for new_x, new_y, result, move_id in new_moves:
                        moves.append((x, y, new_x, new_y, result, move_id))

        return moves

    def move(self, x, y, x2, y2, taken_piece, move_id):
        piece = self.get_piece(x, y)
        if piece:
            # for y in range(8):
            #     for x in range(8):
            #         if self.tiles[x][y] is not None and self.tiles[x][y].is_white == piece.is_white:
            #             self.tiles[x][y].has_just_moved = False
            if taken_piece is not True and taken_piece is not False:
                self.tiles[taken_piece.x][taken_piece.y] = None
            piece.move(move_id)
            self.tiles[x][y] = None
            self.tiles[x2][y2] = piece
            piece.x = x2
            piece.y = y2
        else:
            print('there is no piece')

