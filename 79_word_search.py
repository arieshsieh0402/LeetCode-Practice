from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    path = set()

    def dfs(m, n, i):
        if i == len(word):
            return True
        if (
            (m < 0 or n < 0) or
            (m >= rows or n >= cols) or
            word[i] != board[m][n] or
            (m, n) in path
        ):
            return False

        path.add((m, n))
        is_exist = (
            dfs(m + 1, n, i + 1) or
            dfs(m - 1, n, i + 1) or
            dfs(m, n + 1, i + 1) or
            dfs(m, n - 1, i + 1)
        )
        path.remove((m, n))
        return is_exist

    for m in range(rows):
        for n in range(cols):
            if dfs(m, n, 0):
                return True
    return False
