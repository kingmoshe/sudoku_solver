from typing import List
from time import time

from sudoku_solver.classes.cell import Cell
from sudoku_solver.classes.groups.group import Group


class UniqueGroup(Group):
    TIME = 0

    def __init__(self, cells: List[Cell]):
        super(UniqueGroup, self).__init__(cells)

    def _solve_couples(self) -> bool:
        change = False
        cells = sorted(
            [
                (cell.bin_representation, cell)
                for cell in self.cells
                if len(cell.digits) == 2
            ]
        )
        for i in range(len(cells) - 1):
            first_cell = cells[i][1]
            second_cell = cells[i + 1][1]
            if first_cell.bin_representation == second_cell.bin_representation:
                first_digit, second_digit = tuple(first_cell.digits)
                for cell in self.cells:
                    if cell in [first_cell, second_cell]:
                        continue
                    change = (
                        change
                        or cell.remove_digit(first_digit)
                        or cell.remove_digit(second_digit)
                    )
        return change

    def solve(self) -> bool:
        start_time = time()
        nums = {cell.num for cell in self.cells if cell.is_solved()}
        change = False
        for cell in self.cells:
            if cell.is_solved():
                continue
            for num in nums:
                change = change or cell.remove_digit(num)
        result = change or self._solve_couples()
        UniqueGroup.TIME += time() - start_time
        return result

    def is_solved_correctly(self) -> bool:
        counter = {i: 0 for i in range(1, 10)}
        for cell in self.cells:
            if cell.is_solved():
                counter[cell.num] += 1
        return max(counter.values()) < 2
