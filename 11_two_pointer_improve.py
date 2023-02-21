from typing import List


def max_area(height: List[int]) -> int:
    n = len(height)
    max_container = 0
    left = 0
    right = n - 1

    while left != right:
        max_container = max(
                max_container,
                min(height[left], height[right]) * (right - left)
            )

        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1

    return max_container
