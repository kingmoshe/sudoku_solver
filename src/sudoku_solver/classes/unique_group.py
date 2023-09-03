from sudoku_solver.classes.group import Group


class UniqueGroup(Group):
    def is_valid(self) -> bool:
        found_numbers = [cell.number for cell in self.cells if cell.is_finished]
        return len(found_numbers) == len(set(found_numbers))
