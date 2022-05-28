from typing import List


def smallest_equal(nums: List[int]) -> int:
    """
    Solution of 2057. Smallest Index With Equal Value
    """
    for index, value in enumerate(nums):
        if index % 10 == value:
            return index
    return -1

# URL:https://leetcode.com/problems/smallest-index-with-equal-value/

# ===========Time Complexity(Worst Case Performence)=========== #

# O(n)
