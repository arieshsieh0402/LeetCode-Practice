def climb_stairs_recursion(n: int) -> int:
    def fibonacci(n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci(n)


def climb_stairs_dp(n: int) -> int:
    dp = {1: 1, 2: 2}

    def fibonacci(n: int) -> int:
        nonlocal dp
        if n in dp:
            return dp[n]
        else:
            dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return dp[n]

    return fibonacci(n)


def climb_stairs_one_pass(n: int) -> int:
    if n <= 2:
        return n
    prev_sum, curr_sum = 1, 2
    for _ in range(n - 2):
        # Using swap in Python (tuple packing & unpacking)
        prev_sum, curr_sum = curr_sum, prev_sum + curr_sum
        # Or:
        # temp = prev_sum
        # prev_sum = curr_sum
        # curr_sum = temp + curr_sum
    return curr_sum
