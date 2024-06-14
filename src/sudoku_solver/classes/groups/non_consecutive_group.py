from typing import List

from sudoku_solver.classes.cell import Cell
from sudoku_solver.classes.groups.group import Group


class NonConsecutiveGroup(Group):
    """
    A group of 2 cells that the 2 cells value cannot be consecutive
    currently it can be equal
    """

    def __init__(self, cells: List[Cell]):
        super(NonConsecutiveGroup, self).__init__(cells)

    def solve(self) -> bool:
        change = False
        first_cell = self.cells[0]
        second_cell = self.cells[1]
        if first_cell.is_solved() and second_cell.is_solved():
            return False
        if first_cell.is_solved():
            if (first_cell.num - 1) in second_cell.digits:
                change = True
                second_cell.remove_digit(first_cell.num - 1)
            if (first_cell.num + 1) in second_cell.digits:
                change = True
                second_cell.remove_digit(first_cell.num + 1)
        elif len(first_cell.digits) == 2:
            bigger_digit = max(first_cell.digits)
            smaller_digit = min(first_cell.digits)
            if smaller_digit + 2 == bigger_digit:
                if bigger_digit - 1 in second_cell.digits:
                    change = True
                    second_cell.remove_digit(bigger_digit - 1)

        if second_cell.is_solved():
            if (second_cell.num - 1) in first_cell.digits:
                change = True
                first_cell.remove_digit(second_cell.num - 1)
            if (second_cell.num + 1) in first_cell.digits:
                change = True
                first_cell.remove_digit(second_cell.num + 1)
        elif len(second_cell.digits) == 2:
            bigger_digit = max(second_cell.digits)
            smaller_digit = min(second_cell.digits)
            if smaller_digit + 2 == bigger_digit:
                if bigger_digit - 1 in first_cell.digits:
                    change = True
                    first_cell.remove_digit(bigger_digit - 1)

        return change

    def is_solved_correctly(self) -> bool:
        if self.cells[0].is_solved() and self.cells[1].is_solved():
            first_num = self.cells[0].num
            second_num = self.cells[1].num
            if abs(first_num - second_num) == 1:
                return False
        return True
