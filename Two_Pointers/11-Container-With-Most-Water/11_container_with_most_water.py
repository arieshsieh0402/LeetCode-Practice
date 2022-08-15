from typing import List


def max_area_brute_force(height: List[int]) -> int:
    n = len(height)
    max_container = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            max_container = max(
                    max_container, min(height[i], height[j]) * (j - i)
                )

    return max_container
