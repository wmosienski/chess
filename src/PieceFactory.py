from Move import Move, Placement
from Piece import Piece


def pawn_takes_req(board, piece, dx, dy):
    taken_piece = board.get_piece(piece.x+dx, piece.y+dy)
    if not taken_piece:
        return False
    if not piece.is_white == taken_piece.is_white:
        return taken_piece


def pawn_takes_en_pass_req(board, piece, dx):
    taken_piece = board.get_piece(piece.x + dx, piece.y)
    if not taken_piece:
        return False
    if not piece.is_white == taken_piece.is_white and taken_piece.has_just_moved:
        return taken_piece


def not_occupied_req(board, piece, dx, dy, is_pawn):
    oc_piece = board.get_piece(piece.x+dx, piece.y+dy)
    if not oc_piece:
        return True
    if piece.is_white == oc_piece.is_white:
        return False
    if not piece.is_white == oc_piece.is_white and is_pawn:
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


def create_pawn(x, y, direction):
    pawn = Piece(1, x, y, direction)
    move_forward = Move(0, Placement(0, direction, False, 1),
                        lambda board, piece: not_occupied_req(board, piece, 0, direction, True))
    move_start_forward = Move(0, Placement(0, direction, False, 2),
                        lambda board, piece: chunk_requirements(board, piece, [
                            lambda board, piece: first_move_req(board, piece),
                            lambda board, piece: not_occupied_req(board, piece, 0, direction, True)]))

    pawn_takes_right = Move(0, Placement(1, direction, False, 1),
                        lambda board, piece: pawn_takes_req(board, piece, 1, direction))

    pawn_takes_left = Move(0, Placement(-1, direction, False, 1),
                        lambda board, piece: pawn_takes_req(board, piece, -1, direction))

    pawn_takes_right_en = Move(1, Placement(1, direction, False, 1),
                        lambda board, piece: pawn_takes_en_pass_req(board, piece, 1))

    pawn_takes_left_en = Move(1, Placement(-1, direction, False, 1),
                        lambda board, piece: pawn_takes_en_pass_req(board, piece, -1))

    pawn.add_move(move_forward)
    pawn.add_move(move_start_forward)
    pawn.add_move(pawn_takes_right)
    pawn.add_move(pawn_takes_left)
    pawn.add_move(pawn_takes_right_en)
    pawn.add_move(pawn_takes_left_en)
    return pawn
