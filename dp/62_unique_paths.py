def unique_paths(m: int, n: int) -> int:
    row, col = m, n
    dp = [[1] * col] * row

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[row - 1][col - 1]

# Step
# For the goal grid, only two possibility path to reach it,
# from left grid or top gird.
# Therefore, the path to goal grid is the possibility of from left grid plus
# from top gird.

# It can be represent to:
# path[row][column]=path[row-1][column]+path[row][column-1]

# Create a 2D array as dp and store 1 to all grid temporary.

# Because for the goal at edge, there is only one path, straight right or
# straight down so that we store 1 to every gird on edge.
# Calculate the possibility of rest grid by looping through entire array.

# Return dp[row - 1][col - 1]

# Time Complexity
# O(nm)

# Space Complexity
# O(nm)
