from sudoku_solver.classes.boards.board import Board
from sudoku_solver.classes.groups.non_consecutive_group import NonConsecutiveGroup


def add_non_consecutive_board_groups(board: Board) -> None:
    """
    In Non-Consecutive Sudoku, two directly adjacent cells cannot contain consecutive numbers
    """
    for line_id in range(9):
        for column_id in range(9):
            for y_diff, x_diff in [(1, 0), (0, 1)]:
                new_line_id = line_id + y_diff
                new_column_id = column_id + x_diff
                if max(new_line_id, new_column_id) >= 9:
                    continue
                if min(new_line_id, new_column_id) < 0:
                    continue
                group_cells = [board.cells[line_id][column_id], board.cells[new_line_id][new_column_id]]
                board.add_group(NonConsecutiveGroup(group_cells))
