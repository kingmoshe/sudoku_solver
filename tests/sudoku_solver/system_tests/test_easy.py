import pytest
from tests.sudoku_solver.utils.parser import get_board


@pytest.mark.parametrize('board_name', [
    'easy.txt',
    'medium.txt',
])
def test_easy(board_name):
    easy_board = get_board(board_name)
    easy_board.solve_while_can()
    assert easy_board.is_solved()
