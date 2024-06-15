from typing import List, Tuple
from sudoku_solver.classes.boards.board import Board
from sudoku_solver.classes.groups.unique_group import UniqueGroup
from sudoku_solver.classes.boards.board_types.chess_moves import add_knight_move_board_groups, \
    add_king_move_board_groups
from sudoku_solver.classes.boards.board_types.non_consecutive_board import add_non_consecutive_board_groups


def add_miracle_board_groups(board: Board) -> None:
    """
    Miracle sudoku has the following rules:

    - normal sudoku rules
    - non consecutive rules
    - knight's move
    - kings moves

    This method won't add the normal rules
    """
    add_non_consecutive_board_groups(board)
    add_knight_move_board_groups(board)
    add_king_move_board_groups(board)
