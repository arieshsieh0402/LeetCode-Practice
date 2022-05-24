from typing import List


def search(nums: List[int], target: int) -> int:
    """
    33. Search in Rotated Sorted Array
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        # The array can be divided into the left array and the right array
        # from the flip point.

        # If mid > right, means the hard sorted array may be the left array.
        # So if the target is between left and right,
        # It can find the target by Binary Search.
        # If not, we can find the target in right array.
        elif nums[mid] > nums[right]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # The following code is the opposite way of the above code.
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# URL:https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

# ===========Time Complexity(Worst Case Performence)=========== #

# O(logn)
