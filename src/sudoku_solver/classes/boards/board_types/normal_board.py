from sudoku_solver.classes.boards.board import Board
from sudoku_solver.classes.groups.line_group import LineGroup


def add_line_groups_to_board(board: Board) -> None:
    for line_id in range(9):
        board.add_group(LineGroup([board.cells[line_id][column_id] for column_id in range(9)]))


def add_column_groups_to_board(board: Board) -> None:
    for column_id in range(9):
        board.add_group(LineGroup([board.cells[row_id][column_id] for row_id in range(9)]))


def add_boxes_groups_to_board(board: Board) -> None:
    """
    Add boxes groups

    here line_id represents a line of boxes and column_id represents a column of boxes

    :param board:
    :return:
    """
    for line_id in range(3):
        for column_id in range(3):
            group_cells = []
            for y_diff in range(3):
                for x_diff in range(3):
                    group_cells.append(board.cells[(line_id * 3) + y_diff][(column_id * 3) + x_diff])
            board.add_group(LineGroup(group_cells))


def add_normal_board_groups(board: Board) -> None:
    """
    Add normal board groups (line, column, boxes) same as in a standart sudoku
    """
    add_line_groups_to_board(board)
    add_column_groups_to_board(board)
    add_boxes_groups_to_board(board)

