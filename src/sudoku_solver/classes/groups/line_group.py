from typing import List
from time import time

from sudoku_solver.classes.groups.full_group import FullGroup
from sudoku_solver.classes.groups.unique_group import UniqueGroup
from sudoku_solver.classes.cell import Cell


class LineGroup(FullGroup, UniqueGroup):
    TIME = 0

    def __init__(self, cells: List[Cell]):
        super(LineGroup, self).__init__(cells)

    def solve(self) -> bool:
        start_time = time()
        try:
            result = UniqueGroup.solve(self) or FullGroup.solve(self)
        except Exception as e:
            LineGroup.TIME += time() - start_time
            raise e
        LineGroup.TIME += time() - start_time
        return result

    def is_solved_correctly(self) -> bool:
        return FullGroup.is_solved_correctly(self) and UniqueGroup.is_solved_correctly(self)
