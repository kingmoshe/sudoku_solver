from sudoku_solver.classes.boards.board import Board
from sudoku_solver.classes.groups.line_group import LineGroup


class NormalBoard(Board):
    def __init__(self):
        super(NormalBoard, self).__init__()
        for i in range(9):
            self.add_group(LineGroup([self.cells[i][j] for j in range(9)]))
            self.add_group(LineGroup([self.cells[j][i] for j in range(9)]))
            y = (i // 3) * 3
            x = (i % 3) * 3
            group_cells = [
                self.cells[y + y_dif][x + x_dif]
                for y_dif in range(3)
                for x_dif in range(3)
            ]
            self.add_group(LineGroup(group_cells))
