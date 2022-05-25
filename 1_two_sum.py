from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    nums_dt = {}

    for i in range(len(nums)):
        another_num = target - nums[i]
        # The reason why the value is added to the dict as the key
        # in this place is that when the solution is to return the
        # answer at the end, it will be more complicated to use the
        # value to find the key. And this question assumes that there
        # will only be one solution, so there should be no problem
        # with index being modified.
        if another_num not in nums_dt:
            nums_dt[nums[i]] = i
        else:
            return [nums_dt[another_num], i]

# URL:https://leetcode.com/problems/two-sum/

# ===========Time Complexity(Worst Case Performence)=========== #
# O(n)
