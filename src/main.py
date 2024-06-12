from inputs.parser import get_board
import random
from sudoku_solver.classes.solver import solve_board_recursive
from inputs.special_sodukus.the_ring.creator import board

random.seed(0)
#board = get_board('hard.txt')
#board.solve_while_can()
solve_board_recursive(board, 1, 3)
#solve_board(board)
print(board)
cells = []
for i in range(9):
    for j in range(9):
        cells.append(board.cells[i][j])
for cell in cells:
    if not cell.is_solved():
        print(cell.pos, cell.digits)
