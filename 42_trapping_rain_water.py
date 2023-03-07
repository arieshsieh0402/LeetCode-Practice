from collections import deque
from typing import List


def trap(height: List[int]) -> int:
    n = len(height)
    max_left, max_right = [], deque([])
    curr_max_left, curr_max_right = 0, 0
    water = 0

    for i in range(n):
        max_left.append(curr_max_left)
        curr_max_left = max(curr_max_left, height[i])

    for i in range(n - 1, -1, -1):
        max_right.appendleft(curr_max_right)
        curr_max_right = max(curr_max_right, height[i])

    for i in range(n):
        curr_water = min(max_left[i], max_right[i]) - height[i]
        if curr_water > 0:
            water += curr_water

    return water
