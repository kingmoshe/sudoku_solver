import pytest
from tests.sudoku_solver.utils.parser import get_board


@pytest.fixture
def easy_board():
    return get_board('easy.txt')
