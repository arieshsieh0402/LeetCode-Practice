def unique_paths(m: int, n: int) -> int:
    row, col = m, n
    dp = [[1] * col for _ in range(row)]

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]
