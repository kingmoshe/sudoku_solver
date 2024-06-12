from typing import List

from sudoku_solver.classes.cell import Cell
from sudoku_solver.classes.groups.unique_group import UniqueGroup


class ConsecutiveGroup(UniqueGroup):
    def __init__(self, cells: List[Cell]):
        super(ConsecutiveGroup, self).__init__(cells)

    def solve(self) -> bool:
        change = super(ConsecutiveGroup, self).solve()
        minimal_num = 9
        maximal_num = 1
        for cell in self.cells:
            minimal_num = min(minimal_num, max(cell.digits))
            maximal_num = max(maximal_num, min(cell.digits))
        if maximal_num < minimal_num:
            return change
        maximal_possible_num = minimal_num + len(self.cells) - 1
        minimal_possible_num = maximal_num - len(self.cells) + 1
        for cell in self.cells:
            while min(cell.digits) < minimal_possible_num:
                change = True
                cell.remove_digit(min(cell.digits))
            while max(cell.digits) > maximal_possible_num:
                change = True
                cell.remove_digit(max(cell.digits))
        return change

    def is_solved_correctly(self) -> bool:
        if not super(ConsecutiveGroup, self).is_solved_correctly():
            return False
        if any([cell.is_solved() for cell in self.cells]):
            solved_digits = {cell.num for cell in self.cells if cell.is_solved()}
            if max(solved_digits) - min(solved_digits) >= len(self.cells):
                return False
        return True
