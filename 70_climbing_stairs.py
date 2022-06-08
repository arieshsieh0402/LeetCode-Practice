# Solution 1

def climbStairs(n: int) -> int:
        if n == 1: 
            return 1
        if n == 2:
            return 2
        num = [0] * (n+1)
        num[0] = 0
        num[1] = 1
        num[2] = 2
        # Fibonacci Polynomial
        for i in range(3, n + 1):
            num[i] = num[i-1] + num[i-2]
        return num[i]

# URL:https://leetcode.com/problems/climbing-stairs/

# Time Complexity
# O(n)

# Space
# O(n)

# Solution 2

def climbStairs(n: int) -> int:
        if n == 1: 
            return 1
        if n == 2:
            return 2
        s1, s2 = 1, 2
        # Fibonacci Polynomial
        for _ in range(n - 2):
            s1, s2 = s2, s1 + s2
        return s2

# Time Complexity
# O(n)

# Space
# O(1)
