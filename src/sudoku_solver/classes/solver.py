from copy import deepcopy
import random
import time

from sudoku_solver.utils.time_calculator import calc_time

from sudoku_solver.classes.boards.board import Board

START_TIME = time.time()
COPY_TIME = [0]


def solve_board_recursive(board: Board, amount_of_steps: int, best_guesses_size: int):
    board.solve_while_can()
    if board.is_solved():
        return
    if amount_of_steps == 0:
        return
    guess_times = 0
    while not board.is_solved():
        wrong_guess = None
        best_guesses = []
        for guess in board.get_all_possible_guesses():
            if guess.digit not in guess.cell.digits:
                continue
            new_board = deepcopy(board)
            new_board.cells[guess.cell.i][guess.cell.j].set_num(guess.digit)
            try:
                new_board.solve_while_can()
            except Exception as e:
                wrong_guess = guess
            if (not wrong_guess) and (not new_board.is_solved_correctly()):
                wrong_guess = guess
            guess.set_value(new_board.get_value())
            best_guesses.append(guess)
            if wrong_guess:
                wrong_guess.remove_guess()
                board.solve_while_can()
        if wrong_guess:
            wrong_guess.remove_guess()
            board.solve_while_can()
            continue
        change = False
        best_guesses = sorted(best_guesses)
        best_guesses = best_guesses[:best_guesses_size]
        random.shuffle(best_guesses)
        guess_times += 1
        for guess in best_guesses:
            print("looking at", guess)
            new_board = calc_time(deepcopy, COPY_TIME, board)
            new_board.cells[guess.cell.i][guess.cell.j].set_num(guess.digit)
            try:
                solve_board_recursive(new_board, amount_of_steps - 1, best_guesses_size)
            except Exception as e:
                print("guesses worked")
                guess.remove_guess()
                board.solve_while_can()
                change = True
                break
            if not new_board.is_solved_correctly():
                print("guesses worked")
                guess.remove_guess()
                board.solve_while_can()
                change = True
                break
        if not change:
            return
