from typing import List


def tictactoe(moves: List[List[int]]) -> str:
    win_patterns = [
        [[0, 0], [1, 1], [2, 2]],  # backward_diag
        [[0, 2], [1, 1], [2, 0]],  # forward_diag
        [[0, 0], [0, 1], [0, 2]],  # row_0
        [[1, 0], [1, 1], [1, 2]],  # row_1
        [[2, 0], [2, 1], [2, 2]],  # row_2
        [[0, 0], [1, 0], [2, 0]],  # col_0
        [[0, 1], [1, 1], [2, 1]],  # col_1
        [[0, 2], [1, 2], [2, 2]]   # col_2
    ]

    a = [move for i, move in enumerate(moves) if i % 2 == 0]
    b = [move for i, move in enumerate(moves) if i % 2 == 1]

    for squares_1, squares_2, squares_3 in win_patterns:
        if squares_1 in a and squares_2 in a and squares_3 in a:
            return 'A'
        if squares_1 in b and squares_2 in b and squares_3 in b:
            return 'B'

    return 'Draw' if len(moves) == 9 else 'Pending'
