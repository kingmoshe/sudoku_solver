import pytest
from tests.sudoku_solver.utils.parser import get_board
from sudoku_solver.classes.solver import solve_board_recursive


@pytest.mark.parametrize(
    "board_name",
    [
        "easy.txt",
        "medium.txt",
    ],
)
def test_easy(board_name):
    board = get_board(board_name)
    board.solve_while_can()
    assert board.is_solved()


@pytest.mark.parametrize("board_name", ["hard.txt", "expert.txt"])
def test_complex(board_name):
    board = get_board(board_name)
    solve_board_recursive(board, amount_of_steps=1, best_guesses_size=3)
    assert board.is_solved()
