from tests.sudoku_solver.utils.parser import get_board


def test_easy():
    assert True
    easy_board = get_board('easy.txt')
    easy_board.solve_while_can()
    assert easy_board.is_solved()
