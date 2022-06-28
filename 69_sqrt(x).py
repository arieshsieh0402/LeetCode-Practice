# Brute-Force
def my_sqrt_brute_force(x: int) -> int:
    y = 1
    if x == 0:
        return 0
    elif x == 1:
        return 1
    while True:
        if y * y == x:
            return y
        elif y * y > x:
            return y - 1
        else:
            y += 1


# Binary Search
def my_sqrt_binary_search(x: int) -> int:
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x < (mid + 1)*(mid + 1):
            return mid
        elif x < mid * mid:
            right = mid - 1
        else:
            left = mid + 1
