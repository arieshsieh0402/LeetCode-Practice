def minimum_total(triangle):
    '''
    [
    [2]
    [3, 4]
    [6, 5, 7]
    [4, 1, 8, 3]
    ]
    r = rows
    e = elements
    '''
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    for r in range(len(triangle)):
        for e in range(len(triangle[r])):
            # Top of the triangle
            if r == 0 and e == 0:
                dp[r][e] = triangle[r][e]
            # For the first element of a row
            # The possibility of path from the previous row
            # is only can dp[r - 1][e]
            elif e == 0:
                dp[r][e] = triangle[r][e] + dp[r - 1][e]
            # For the last element of a row
            # The possibility of path from the previous row
            # is only can dp[r - 1][e - 1]
            elif e == len(triangle[r]) - 1:
                dp[r][e] = triangle[r][e] + dp[r - 1][e - 1]
            else:
                dp[r][e] = triangle[r][e] + min(dp[r - 1][e], dp[r - 1][e - 1])

    return min(dp[-1])
