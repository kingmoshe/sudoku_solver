from typing import Optional


class Cell:
    SIZE = 9

    def __init__(self, number: Optional[int] = None):
        self._cell_options = [True for _ in range(Cell.SIZE + 1)]
        self._cell_options[0] = False
        self._remaining_options_amount = Cell.SIZE
        self.number = number
        if self.number:
            self._cell_options = [i == number for i in range(Cell.SIZE + 1)]
            self._remaining_options_amount = 1

    def is_finished(self) -> bool:
        return self.number is not None

    def remove_option(self, option: int) -> bool:
        if self._cell_options[option]:
            self._cell_options[option] = False
            self._remaining_options_amount -= 1
            if self._remaining_options_amount == 1:
                self.number = self._cell_options.index(True)
            return True
        return False
