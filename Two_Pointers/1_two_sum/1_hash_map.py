from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    nums_dt = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dt:
            return [nums_dt[complement], i]
        nums_dt[num] = i
