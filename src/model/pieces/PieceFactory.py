from src.model.moves.Move import Move, Placement
from src.model.pieces.Piece import Piece


def pawn_takes_req(board, piece, dx, dy):
    taken_piece = board.get_piece(piece.x+dx, piece.y+dy)
    if not taken_piece:
        return False
    if not piece.is_white == taken_piece.is_white:
        return taken_piece
    return False


def pawn_takes_en_pass_req(board, piece, dx):
    taken_piece = board.get_piece(piece.x + dx, piece.y)
    if not taken_piece:
        return False
    if not piece.is_white == taken_piece.is_white and taken_piece.has_just_moved and taken_piece.last_move_id == PAWN_MOVE_START_FORWARD_ID:
        return taken_piece
    return False


def not_occupied_req(board, piece, dx, dy, is_pawn):
    oc_piece = board.get_piece(piece.x+dx, piece.y+dy)
    if not oc_piece:
        return True
    if piece.is_white == oc_piece.is_white:
        return False
    if not piece.is_white == oc_piece.is_white and is_pawn:
        return False
    if not piece.is_white == oc_piece.is_white and not is_pawn:
        return oc_piece
    return False


def first_move_req(board, piece):
    return not piece.has_moved


def chunk_requirements(board, piece, requirements):
    result = True
    for req in requirements:
        req_result = req(board, piece)
        if not req_result:
            return False
        elif not req_result == True and not req_result == False:
            result = req_result
    return result

PAWN_MOVE_START_FORWARD_ID = 1

def create_pawn(x, y, direction):
    pawn = Piece(1, x, y, direction)
    move_forward = Move(0, Placement(0, direction, False, 1),
                        lambda board, piece, dx, dy: not_occupied_req(board, piece, dx, dy, True))
    move_start_forward = Move(PAWN_MOVE_START_FORWARD_ID, Placement(0, direction, False, 2),
                        lambda board, piece, dx, dy: chunk_requirements(board, piece, [
                            lambda board, piece: first_move_req(board, piece),
                            lambda board, piece: not_occupied_req(board, piece, dx, dy, True)]))

    pawn_takes_right = Move(0, Placement(1, direction, False, 1),
                        lambda board, piece, dx, dy: pawn_takes_req(board, piece, dx, dy))

    pawn_takes_left = Move(0, Placement(-1, direction, False, 1),
                        lambda board, piece, dx, dy: pawn_takes_req(board, piece, dx, dy))

    pawn_takes_right_en = Move(0, Placement(1, direction, False, 1),
                        lambda board, piece, dx, dy: pawn_takes_en_pass_req(board, piece, 1))

    pawn_takes_left_en = Move(0, Placement(-1, direction, False, 1),
                        lambda board, piece, dx, dy: pawn_takes_en_pass_req(board, piece, -1))

    pawn.add_move(move_forward)
    pawn.add_move(move_start_forward)
    pawn.add_move(pawn_takes_right)
    pawn.add_move(pawn_takes_left)
    pawn.add_move(pawn_takes_right_en)
    pawn.add_move(pawn_takes_left_en)
    return pawn


def create_rook(x, y, direction):
    rook = Piece(4, x, y, direction)
    move_up = Move(0, Placement(0, 1, True, 1),
                        lambda board, piece, dx, dy: not_occupied_req(board, piece, dx, dy, False))
    move_right = Move(0, Placement(1, 0, True, 1),
                        lambda board, piece, dx, dy: not_occupied_req(board, piece, dx, dy, False))
    move_left = Move(0, Placement(-1, 0, True, 1),
                        lambda board, piece, dx, dy: not_occupied_req(board, piece, dx, dy, False))
    move_down = Move(0, Placement(0, -1, True, 1),
                        lambda board, piece, dx, dy: not_occupied_req(board, piece, dx, dy, False))

    rook.add_move(move_up)
    rook.add_move(move_right)
    rook.add_move(move_left)
    rook.add_move(move_down)
    return rook


def create_bishop(x, y, direction):
    bishop = Piece(3, x, y, direction)
    move_up_right = Move(0, Placement(1, 1, True, 1),
                        lambda board, piece, dx, dy: not_occupied_req(board, piece, dx, dy, False))
    move_down_right = Move(0, Placement(1, -1, True, 1),
                        lambda board, piece, dx, dy: not_occupied_req(board, piece, dx, dy, False))
    move_up_left = Move(0, Placement(-1, 1, True, 1),
                        lambda board, piece, dx, dy: not_occupied_req(board, piece, dx, dy, False))
    move_down_left = Move(0, Placement(-1, -1, True, 1),
                        lambda board, piece, dx, dy: not_occupied_req(board, piece, dx, dy, False))

    bishop.add_move(move_up_right)
    bishop.add_move(move_down_right)
    bishop.add_move(move_up_left)
    bishop.add_move(move_down_left)
    return bishop
