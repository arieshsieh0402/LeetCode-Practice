# Solution 1
# Fibonacci Recursive


def climb_stairs(n: int) -> int:
    # Base case
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)

# Time Complexity: O(2^n)

# With each successive tree level, our n reduces by 1.
# Thus our tree will have a depth of n before it reaches the base case.
# Since each node has 2 branches and we have n total levels,
# our total number of nodes is 2^n making our time complexity O(2^n).

# Space Complexity: O(n)

# Our memory complexity is determined by the number of return statements
# because each function call will be stored on the program stack.
# To generalize, a recursive function's memory complexity is O(recursion depth)
# As our tree depth suggests, we will have n total return statements and thus
# the memory complexity is O(n).


# Solution 2
# Fibonacci with DP


dp = {1: 1, 2: 2}
def climb_stairs(n: int) -> int:
    if n in dp:
        return dp[n]
    else:
        dp[n] = climb_stairs(n - 1) + climb_stairs(n - 2)
        return dp[n]

# Time Complexity: O(n)

# The times of recursion is n (until base case).

# Space Complexity: O(n)

# 2n (n of dp + n of recursion)

# Solution 3
# Fibonacci with DP in iteration way

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[i]


# Time Complexity: O(n)

# The times of iteration is n.

# Space Complexity: O(n)

# 2n (n of dp + n of iteration)


# Solution 4
# Fibonacci with DP in tricky way

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    s1, s2 = 1, 2
    for _ in range(n - 2):
        # Using swap in Python (tuple packing & unpacking)
        s1, s2 = s2, s1 + s2
        # Or:
        # temp = s1
        # s1 = s2
        # s2 = temp + s2
    return s2

# Time Complexity: O(n)

# The times of iteration is n.

# Space: O(1)

# set two variables s1 and s2.
# in each iteration, assign s2 to s1, s1 + s2 to s2.
