# Given an integer array nums, find the contiguous sub array
# (containing at least one number)
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

from typing import List


def max_sub_array(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    max_sum = nums[0]
    cur_sum = 0
    for num in nums:
        # Compare the current sum with the current number,
        # if the current number is larger,
        # it means that the current sum will not be the best subarray.
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)
    return max_sum

# URL:https://leetcode.com/problems/maximum-subarray/

# Time Complexity
# O(n)

# Space
# O(1)
