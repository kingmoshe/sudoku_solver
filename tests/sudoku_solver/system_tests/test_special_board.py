import pytest
from tests.sudoku_solver.utils.parser import get_board
from sudoku_solver.classes.boards.board_types.non_consecutive_board import add_non_consecutive_board_groups


@pytest.mark.parametrize(
    "board_name",
    [
        "puzzle_1.txt",
    ],
)
def test_non_consecutive(board_name):
    board = get_board(board_name, resource_path="../../resources/miracle_sudokus")
    add_non_consecutive_board_groups(board)
    board.solve_while_can()
    print()
    print(board)
    assert board.is_solved()
