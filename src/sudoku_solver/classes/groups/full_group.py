from typing import List
from time import time

from sudoku_solver.classes.groups.group import Group
from sudoku_solver.classes.cell import Cell


class FullGroup(Group):
    TIME = 0
    GET_COUNTER_TIME = 0
    FIND_COUPLES_TIME = 0

    def __init__(self, cells: List[Cell]):
        super(FullGroup, self).__init__(cells)

    def _get_counter(self):
        start_time = time()
        values = [cell.bin_representation // 2 for cell in self.cells]
        counter = {i: 0 for i in range(1, 10)}
        for dig in range(1, 10):
            counter[dig] = sum([val % 2 for val in values])
            values = [val // 2 for val in values]
        FullGroup.GET_COUNTER_TIME += time() - start_time
        return counter

    def _find_couples(self, counter=None) -> bool:
        start_time = time()
        change = False
        counter = counter or self._get_counter()
        good_digits = [key for key, value in counter.items() if value == 2]
        for first_digit in good_digits:
            for second_digit in good_digits:
                if second_digit <= first_digit:
                    continue
                good_cells = [
                    cell
                    for cell in self.cells
                    if first_digit in cell.digits and second_digit in cell.digits
                ]
                if len(good_cells) == 2:
                    for cell in good_cells:
                        bad_digits = {
                            dig
                            for dig in cell.digits
                            if dig not in [first_digit, second_digit]
                        }
                        for dig in bad_digits:
                            change = change or cell.remove_digit(dig)
        FullGroup.FIND_COUPLES_TIME += time() - start_time
        return change

    def solve(self) -> bool:
        start_time = time()
        change = False
        counter = self._get_counter()
        bad_digits = {cell.num for cell in self.cells if cell.is_solved()}
        for digit, times in counter.items():
            if digit in bad_digits:
                continue
            if times == 1:
                for cell in self.cells:
                    if (2**digit) & cell.bin_representation:
                        change = change or cell.set_num(digit)
        result = change or self._find_couples(counter)
        FullGroup.TIME += time() - start_time
        return result

    def is_solved_correctly(self) -> bool:
        val = 0
        for cell in self.cells:
            val = val | cell.bin_representation
        return val == 1022
