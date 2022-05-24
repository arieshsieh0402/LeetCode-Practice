from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif nums[mid] > nums[right]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# URL:https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

# ===========Time Complexity(Worst Case Performence)=========== #

# O(logn)
