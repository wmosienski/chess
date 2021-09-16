

class Move:
    def __init__(self, id, placement, requirement_func):
        self.id = id
        self.placement = placement
        self.requirement_func = requirement_func

    def get_possible_tiles(self, board, piece):
        tiles = []
        for x, y in self.placement.get_possible_tiles(piece.x, piece.y):
            result = self.requirement_func(board, piece, x-piece.x, y-piece.y)
            # print(result)
            if result:
                tiles.append((x, y, result, self.id))
            if result is not True:
                break

        return tiles


class Placement:
    def __init__(self, dx, dy, is_repeatable, times):
        self.times = times
        self.dx = dx
        self.dy = dy
        self.is_repeatable = is_repeatable

    def get_possible_tiles(self, x, y):
        tiles = []
        new_x = x + self.dx
        new_y = y + self.dy
        while 8 > new_x >= 0 and 8 > new_y >= 0:
            for i in range(self.times):
                tiles.append((new_x, new_y))
                new_x = new_x + self.dx
                new_y = new_y + self.dy
            if not self.is_repeatable:
                break

        return tiles


