from time import time
from typing import List

from sudoku_solver.classes.position import Position
from sudoku_solver.classes.exceptions.empty_cell import EmptyCell


class Cell:
    KEYS_TO_NUM = {2**i: i for i in range(1, 10)}
    KEYS_TO_DIGITS = {}
    REMOVE_DICT = {}
    TIME = 0

    def __init__(self, pos: Position):
        self.pos = pos
        self.bin_representation = (2**10) - 2
        self.num = 0

    def remove_digit(self, digit: int) -> bool:
        key = (self.bin_representation, digit)
        if not Cell.REMOVE_DICT.get(key, True):
            return False
        if not ((2**digit) & self.bin_representation):
            Cell.REMOVE_DICT[key] = False
            return False
        elif self.bin_representation == 2**digit:
            raise EmptyCell(self.pos)
        self.bin_representation -= 2**digit
        self.num = Cell.KEYS_TO_NUM.get(self.bin_representation, 0)
        return True

    def is_solved(self) -> bool:
        return self.num != 0

    def set_num(self, digit: int) -> bool:
        if not ((2**digit) & self.bin_representation):
            raise EmptyCell(self.pos)
        if self.is_solved():
            return False
        self.num = digit
        self.bin_representation = 2**digit
        return True

    @property
    def digits(self) -> List[int]:
        start_time = time()
        if self.bin_representation not in Cell.KEYS_TO_DIGITS:
            Cell.KEYS_TO_DIGITS[self.bin_representation] = {
                i for i in range(1, 10) if self.bin_representation & (2**i)
            }
        result = Cell.KEYS_TO_DIGITS[self.bin_representation]
        Cell.TIME += time() - start_time
        return result

    @property
    def i(self):
        return self.pos.i

    @property
    def j(self):
        return self.pos.j

    def __eq__(self, other):
        return isinstance(other, Cell) and self.pos == other.pos

    def __lt__(self, other):
        return self.pos < other.pos
