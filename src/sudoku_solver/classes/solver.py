from copy import deepcopy
import random
import time

from sudoku_solver.utils.time_calculator import calc_time

from sudoku_solver.classes.boards.board import Board
from sudoku_solver.classes.boards.guess import Guess

START_TIME = time.time()
COPY_TIME = [0]


def _try_solving_taking_one_guess(board: Board, guess: Guess) -> bool:
    """
    Try solving board while taking 1 guess and checking if there is a problem/solution

    :return: True if board was somehow changed
    """
    # If the digit was already removed or the guess was already made
    if (guess.digit not in guess.cell.digits) or (guess.cell.num == guess.digit):
        return False
    new_board = deepcopy(board)
    new_board.cells[guess.cell.i][guess.cell.j].set_num(guess.digit)
    try:
        new_board.solve_while_can()
        assert board.is_solved_correctly()
    except Exception as e:
        guess.remove_guess()
        return True
    if new_board.is_solved():
        guess.make_guess()
        return True
    return False


def solve_one_guess_while_can(board: Board) -> bool:
    any_change = board.solve_while_can()
    change = True
    while change and not (board.is_solved()):
        change = False
        for guess in board.get_all_possible_guesses():
            if _try_solving_taking_one_guess(board, guess):
                change = True
                any_change = True
                board.solve_while_can()
    return any_change


def solve_board_recursive(board: Board, amount_of_steps: int, best_guesses_size: int):
    board.solve_while_can()
    if board.is_solved():
        return
    if amount_of_steps == 0:
        return
    while not board.is_solved():
        change = solve_one_guess_while_can(board)
        if change:
            continue
        break
        # best_guesses = []
        # for guess in board.get_all_possible_guesses():
        #     best_guesses.append()
        # change = False
        # best_guesses = sorted(best_guesses)
        # best_guesses = best_guesses[:best_guesses_size]
        # random.shuffle(best_guesses)
        # guess_times += 1
        # for guess in best_guesses:
        #     print("looking at", guess)
        #     new_board = calc_time(deepcopy, COPY_TIME, board)
        #     new_board.cells[guess.cell.i][guess.cell.j].set_num(guess.digit)
        #     try:
        #         solve_board_recursive(new_board, amount_of_steps - 1, best_guesses_size)
        #     except Exception as e:
        #         print("guesses worked")
        #         guess.remove_guess()
        #         board.solve_while_can()
        #         change = True
        #         break
        #     if not new_board.is_solved_correctly():
        #         print("guesses worked")
        #         guess.remove_guess()
        #         board.solve_while_can()
        #         change = True
        #         break
        # if not change:
        #     return
