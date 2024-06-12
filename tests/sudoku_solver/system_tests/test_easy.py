from sudoku_solver.classes.board import Board
from tests.sudoku_solver.utils.parser import get_board
#board = get_board('..\special_sodukus\\the_ring\\soduku.txt')
board = get_board('easy.txt')
print(board)


def test_easy(easy_board: Board):
    easy_board.solve_while_can()
    assert easy_board.is_solved()
