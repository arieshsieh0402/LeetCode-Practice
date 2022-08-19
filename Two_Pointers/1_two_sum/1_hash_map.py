from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    nums_dt = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement not in nums_dt:
            nums_dt[complement] = i
        else:
            return [nums_dt[complement], i]
