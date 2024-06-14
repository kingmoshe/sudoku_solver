from pathlib import Path
import os

from sudoku_solver.classes.boards.board import Board
from sudoku_solver.classes.boards.board_types.normal_board import NormalBoard
from sudoku_solver.classes.position import Position


def get_board(name: str) -> Board:
    b = NormalBoard()
    cur_path = Path(os.path.abspath(__file__))
    path = cur_path.parent.parent / "resources" / "sodukus" / name
    with open(path, "r") as f:
        lines = f.readlines()
    lines = [list(map(int, line.replace("\n", "").split())) for line in lines]
    for i in range(9):
        for j in range(9):
            if lines[i][j] != 0:
                b.add_num(Position(i, j), lines[i][j])
    return b
