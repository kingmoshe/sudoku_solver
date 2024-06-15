import pytest
from tests.sudoku_solver.utils.parser import get_board
from sudoku_solver.classes.solver import solve_board_recursive
from sudoku_solver.classes.boards.board_types.non_consecutive_board import add_non_consecutive_board_groups
from sudoku_solver.classes.boards.board_types.miracle_board import add_miracle_board_groups


@pytest.mark.parametrize(
    "board_name",
    [
        "puzzle_1.txt",
        "puzzle_5.txt",
        "puzzle_7.txt",
        "puzzle_12.txt",
        "puzzle_15.txt",
        "puzzle_61.txt",
        "puzzle_63.txt",
    ],
)
def test_non_consecutive(board_name):
    board = get_board(board_name, resource_path="../../resources/miracle_sudokus")
    add_non_consecutive_board_groups(board)
    board.solve_while_can()
    print()
    print(board)
    assert board.is_solved()


@pytest.mark.parametrize(
    "board_name",
    [
        "puzzle_8.txt",
        "puzzle_10.txt",
        "puzzle_29.txt",
        "puzzle_35.txt",
        "puzzle_38.txt",
        "puzzle_49.txt",
        "puzzle_54.txt",
        "puzzle_58.txt",
        "puzzle_70.txt",
        "puzzle_76.txt",
        "puzzle_93.txt",
    ],
)
def test_non_consecutive_complex(board_name):
    board = get_board(board_name, resource_path="../../resources/miracle_sudokus")
    add_non_consecutive_board_groups(board)
    solve_board_recursive(board, amount_of_steps=1, best_guesses_size=3)
    assert board.is_solved()


@pytest.mark.parametrize(
    "board_name",
    [
        "puzzle_4.txt",
    ],
)
def test_miracle_sudoku(board_name):
    board = get_board(board_name, resource_path="../../resources/miracle_sudokus")
    add_miracle_board_groups(board)
    board.solve_while_can()
    assert board.is_solved()


@pytest.mark.parametrize(
    "board_name",
    [
        "puzzle_6.txt",
        "puzzle_13.txt",
        "puzzle_17.txt",
        "puzzle_22.txt",
        "puzzle_26.txt",
        "puzzle_32.txt",
        "puzzle_34.txt",
        "puzzle_37.txt",
        "puzzle_40.txt",
        "puzzle_68.txt",
    ],
)
def test_miracle_sudoku_complex(board_name):
    board = get_board(board_name, resource_path="../../resources/miracle_sudokus")
    add_miracle_board_groups(board)
    solve_board_recursive(board, amount_of_steps=1, best_guesses_size=3)
    assert board.is_solved()
