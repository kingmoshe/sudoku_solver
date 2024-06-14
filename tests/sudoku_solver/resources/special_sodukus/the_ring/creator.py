from sudoku_solver.utils.parser import get_board
from sudoku_solver.classes.groups.arrow_group import ArrowGroup
from sudoku_solver.classes.groups.consecutive_group import ConsecutiveGroup

board = get_board("..\special_sodukus\\the_ring\\soduku.txt")

arrow_groups = []
consecutive_groups = []

arrow_groups.append(
    ArrowGroup(
        board.get_cell(2, 2),
        [board.get_cell(0, 0), board.get_cell(0, 1), board.get_cell(1, 1)],
    )
)
arrow_groups.append(
    ArrowGroup(
        board.get_cell(2, 6),
        [board.get_cell(0, 8), board.get_cell(1, 7), board.get_cell(1, 8)],
    )
)
arrow_groups.append(
    ArrowGroup(
        board.get_cell(6, 2),
        [board.get_cell(8, 0), board.get_cell(7, 0), board.get_cell(7, 1)],
    )
)
arrow_groups.append(
    ArrowGroup(
        board.get_cell(6, 6),
        [board.get_cell(7, 7), board.get_cell(8, 7), board.get_cell(8, 8)],
    )
)

arrow_groups.append(ArrowGroup(board.get_cell(2, 2), [board.get_cell(3, 3)]))
arrow_groups.append(ArrowGroup(board.get_cell(2, 6), [board.get_cell(3, 5)]))
arrow_groups.append(ArrowGroup(board.get_cell(6, 2), [board.get_cell(5, 3)]))
arrow_groups.append(ArrowGroup(board.get_cell(6, 6), [board.get_cell(5, 5)]))

consecutive_groups.append(
    ConsecutiveGroup([board.get_cell(0, 3), board.get_cell(1, 4), board.get_cell(0, 5)])
)
consecutive_groups.append(
    ConsecutiveGroup(
        [
            board.get_cell(2, 3),
            board.get_cell(2, 4),
            board.get_cell(2, 5),
            board.get_cell(3, 4),
        ]
    )
)
consecutive_groups.append(
    ConsecutiveGroup([board.get_cell(2, 8), board.get_cell(3, 7), board.get_cell(3, 8)])
)
consecutive_groups.append(
    ConsecutiveGroup(
        [
            board.get_cell(3, 2),
            board.get_cell(4, 2),
            board.get_cell(5, 2),
            board.get_cell(4, 3),
        ]
    )
)
consecutive_groups.append(
    ConsecutiveGroup([board.get_cell(4, 4), board.get_cell(4, 5)])
)
consecutive_groups.append(
    ConsecutiveGroup([board.get_cell(3, 6), board.get_cell(4, 6), board.get_cell(5, 6)])
)
consecutive_groups.append(
    ConsecutiveGroup([board.get_cell(6, 3), board.get_cell(6, 4), board.get_cell(6, 5)])
)
consecutive_groups.append(
    ConsecutiveGroup([board.get_cell(7, 3), board.get_cell(8, 3)])
)
consecutive_groups.append(
    ConsecutiveGroup([board.get_cell(8, 5), board.get_cell(8, 6)])
)

for group in arrow_groups:
    board.add_group(group)
for group in consecutive_groups:
    board.add_group(group)
