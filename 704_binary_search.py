from typing import List


def search(nums: List[int], target: int) -> int:
    """Binary Search"""
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2

    while left <= right:
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        mid = (left + right) // 2

    return -1

# URL:https://leetcode.com/problems/binary-search/

# ===========Time Complexity(Worst Case Performence)=========== #

# O(logn)
