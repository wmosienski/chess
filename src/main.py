from Board import Board
import random
if __name__ == '__main__':
    board = Board()
    board.setPieces()
    is_white = True
    while True:
        board.print()
        action = input('press enter to continue, space to restart, anything else to quit')
        if action == '':
            moves = board.get_all_moves(is_white)
            x, y, x2, y2, result = moves[random.randint(0, len(moves)-1)]
            board.move(x, y, x2, y2, result)
            is_white = not is_white
        elif action == ' ':
            board = Board()
            board.setPieces()
            is_white = True
        else:
            break


