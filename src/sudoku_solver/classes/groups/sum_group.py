from typing import List

from sudoku_solver.classes.cell import Cell
from sudoku_solver.classes.groups.group import Group


class SumGroup(Group):
    def __init__(self, cells: List[Cell], sum: int):
        super(SumGroup, self).__init__(cells)
        self.sum = sum

    def solve(self) -> bool:
        change = False
        maximal_sum = self.maximal_possible_sum()
        minimal_sum = self.minimal_possible_sum()
        for cell in self.cells:
            temp_max_sum = maximal_sum - max(cell.digits)
            temp_min_sum = minimal_sum - min(cell.digits)
            while temp_max_sum + min(cell.digits) < self.sum:
                cell.remove_digit(min(cell.digits))
                change = True
            while temp_min_sum + max(cell.digits) > self.sum:
                cell.remove_digit(max(cell.digits))
                change = True
        return change

    def maximal_possible_sum(self) -> int:
        return sum([max(cell.digits) for cell in self.cells])

    def minimal_possible_sum(self) -> int:
        return sum([min(cell.digits) for cell in self.cells])

    def is_solved_correctly(self) -> bool:
        return self.minimal_possible_sum() <= self.sum <= self.maximal_possible_sum()
