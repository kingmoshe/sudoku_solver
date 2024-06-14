from typing import List
import random

from sudoku_solver.classes.cell import Cell
from sudoku_solver.classes.boards.guess import Guess
from sudoku_solver.classes.position import Position
from sudoku_solver.classes.groups.group import Group
from sudoku_solver.classes.boards.board_val import BoardVal


class Board:
    def __init__(self):
        self.cells = [[Cell(Position(i, j)) for j in range(9)] for i in range(9)]
        self.groups = []

    def get_value(self):
        return BoardVal(list(map(len, [cell.digits for cell in self.all_cells])))

    def get_all_possible_guesses(self) -> List[Guess]:
        guesses = []
        for cell in self.all_cells:
            if not cell.is_solved():
                for digit in cell.digits:
                    guesses.append(Guess(cell, digit))
        random.shuffle(guesses)
        return guesses

    def get_cell(self, i: int, j: int) -> Cell:
        return self.cells[i][j]

    def add_num(self, pos: Position, num: int) -> None:
        self.cells[pos.i][pos.j].set_num(num)

    def add_group(self, group: Group) -> None:
        self.groups.append(group)

    def solve(self) -> bool:
        return any([group.solve() for group in self.groups])

    def solve_while_can(self) -> bool:
        change = False
        while any([group.solve_while_can() for group in self.groups]):
            change = True
        any([group.solve_while_can() for group in self.groups])
        return change

    def is_solved(self) -> bool:
        return all([cell.is_solved() for cell in self.all_cells])

    def is_solved_correctly(self) -> bool:
        return all(group.is_solved_correctly() for group in self.groups)

    @property
    def all_cells(self) -> List[Cell]:
        cells = []
        for i in range(9):
            cells += self.cells[i]
        return cells

    def __repr__(self) -> str:
        return "\n".join(
            [
                " ".join(map(str, [self.cells[i][j].num for j in range(9)]))
                for i in range(9)
            ]
        )
