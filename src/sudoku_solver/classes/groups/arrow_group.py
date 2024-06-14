from typing import List
from time import time

from sudoku_solver.classes.groups.group import Group
from sudoku_solver.classes.cell import Cell


class ArrowGroup(Group):
    TIME = 0

    def __init__(self, sum_cell: Cell, cells: List[Cell]):
        super(ArrowGroup, self).__init__(cells)
        self.sum_cell = sum_cell

    def solve(self) -> bool:
        start_time = time()
        change = False
        min_sum = self.minimal_possible_sum()
        max_sum = self.maximal_possible_sum()
        while min_sum > min(self.sum_cell.digits):
            change = True
            self.sum_cell.remove_digit(min(self.sum_cell.digits))
        while max_sum < max(self.sum_cell.digits):
            change = True
            self.sum_cell.remove_digit(max(self.sum_cell.digits))
        for cell in self.cells:
            temp_max_sum = max_sum - max(cell.digits)
            while min(cell.digits) + temp_max_sum < min(self.sum_cell.digits):
                cell.remove_digit(min(cell.digits))
                change = True
            temp_min_sum = min_sum - min(cell.digits)
            while max(cell.digits) + temp_min_sum > max(self.sum_cell.digits):
                cell.remove_digit(max(cell.digits))
                change = True
            max_sum = temp_max_sum + max(cell.digits)
            min_sum = temp_min_sum + min(cell.digits)
        ArrowGroup.TIME += time() - start_time
        return change

    def maximal_possible_sum(self) -> int:
        return sum([max(cell.digits) for cell in self.cells])

    def minimal_possible_sum(self) -> int:
        return sum([min(cell.digits) for cell in self.cells])

    def is_solved_correctly(self) -> bool:
        return (
            self.minimal_possible_sum() <= max(self.sum_cell.digits)
            and min(self.sum_cell.digits) <= self.maximal_possible_sum()
        )
