from typing import List, Tuple
from sudoku_solver.classes.boards.board import Board
from sudoku_solver.classes.groups.line_group import LineGroup

KNIGHT_VECTORS: List[Tuple[int, int]] = [(1, -2), (2, -1), (2, 1),
                                         (1, 2)]  # Only one direction (to not add the same group twice)
KING_VECTORS: List[Tuple[int, int]] = [(0, 1), (1, -1), (1, 0),
                                       (1, 1)]  # Only one direction (to not add the same group twice)


def _add_chess_move_board_group(board: Board, move_vectors: List[Tuple[int, int]]) -> None:
    """
    add chess move board groups
    :param board:
    :param move_vectors: The type of step legal by the specific chess move
    """
    for line_id in range(9):
        for column_id in range(9):
            for y_diff, x_diff in move_vectors:
                new_line_id = line_id + y_diff
                new_column_id = column_id + x_diff
                if max(new_line_id, new_column_id) >= 9:
                    continue
                if min(new_line_id, new_column_id) < 0:
                    continue
                group_cells = [board.cells[line_id][column_id], board.cells[new_line_id][new_column_id]]
                board.add_group(LineGroup(group_cells))


def add_knight_move_board_groups(board: Board) -> None:
    """
    Add knight board groups, two cells in a knight step between them should not be equal
    """
    _add_chess_move_board_group(board, KNIGHT_VECTORS)


def add_king_move_board_groups(board: Board) -> None:
    """
    Add knight board groups, two cells in a chess step between them should not be equal
    """
    _add_chess_move_board_group(board, KING_VECTORS)
