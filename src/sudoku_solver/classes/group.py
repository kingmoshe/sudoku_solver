from typing import List
from sudoku_solver.classes.cell import Cell


class Group:
    def __init__(self, cells: List[Cell]):
        self.cells = cells

    @property
    def is_finished(self) -> bool:
        return all(cell.is_finished for cell in self.cells)

    def is_valid(self) -> bool:
        """
        Check if the group cells are currently valid
        """
        raise NotImplementedError()
