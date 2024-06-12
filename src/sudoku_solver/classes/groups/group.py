from typing import List
from sudoku_solver.classes.cell import Cell


class Group:
    def __init__(self, cells: List[Cell]):
        self.cells = cells

    def solve(self) -> bool:
        """
        Try to find some meaningfull changes,
        :return: True if some change was found
        """
        raise NotImplemented("Group has no solve")

    def solve_while_can(self) -> bool:
        change = False
        while self.solve():
            change = True
        return change

    def is_solved(self) -> bool:
        return all([cell.is_solved() for cell in self.cells])

    def is_solved_correctly(self) -> bool:
        """
        Check if the current solution is ok
        :return: False if the group cannot be solved in the current status
        """
        raise NotImplemented("Group has no is solved correctly")
