from collections import deque
from typing import List


def num_islands_dfs(grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    islands = 0

    def dfs(i, j):
        nonlocal m, n, islands
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                islands += 1
                dfs(i, j)
    return islands


def num_islands(grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    islands = 0
    q = deque([])

    for i in range(m):
        for j in range(n):
            if grid[i][j] != '1':
                continue
            islands += 1
            q.append((i, j))
            while q:
                (x, y) = q.popleft()
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    grid[x][y] = '0'
                    q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return islands
