from sudoku_solver.classes.cell import Cell


class Guess:
    def __init__(self, cell: Cell, digit: int):
        self.cell = cell
        self.digit = digit
        self.value = None

    def set_value(self, value: int):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def remove_guess(self):
        self.cell.remove_digit(self.digit)

    def __repr__(self):
        return str(self.cell.pos) + ' ' + str(self.digit)
