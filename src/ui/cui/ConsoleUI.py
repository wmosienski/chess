

class ConsoleUI:
    def __init__(self, model):
        self.model = model
        self.piece_char_map = {
            1: '♙',
            3: '♗',
            4: '♖',
            -1: '♟',
            -3: '♝',
            -4: '♜',
        }

    def render(self):
        for y in range(8):
            output = ""
            for x in range(8):
                if self.model.board.tiles[x][7-y] is not None:
                    output += "" + self.piece_char_map[self.get_piece_key(self.model.board.tiles[x][7 - y])] + " "
                else:
                    output += " " + " "

            print(output)


    def get_piece_key(self, piece):
        return piece.id*piece.direction

