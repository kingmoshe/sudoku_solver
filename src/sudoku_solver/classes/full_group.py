from sudoku_solver.classes.group import Group
from sudoku_solver.classes.cell import Cell


class FullGroup(Group):
    def is_valid(self) -> bool:
        """
        Check that every number is still a remaining option for some cell.
        """
        options = set()
        for cell in self.cells:
            options = options.union(cell.remaining_options)
            if len(options) == Cell.SIZE:
                return True
        return False
