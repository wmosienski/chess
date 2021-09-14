

class ConsoleUI:
    def __init__(self, model):
        self.model = model

    def render(self):
        for y in range(8):
            output = ""
            for x in range(8):
                if self.model.board.tiles[x][7-y] is not None:
                    output += str(self.model.board.tiles[x][7-y].id) + "  "
                else:
                    output += "_" + "  "

            print(output)
