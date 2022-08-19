from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])

    left = 0
    right = len(sorted_nums) - 1

    while left < right:
        if target == sorted_nums[left][0] + sorted_nums[right][0]:
            return [sorted_nums[left][1], sorted_nums[right][1]]
        elif target > sorted_nums[left][0] + sorted_nums[right][0]:
            left += 1
        else:
            right -= 1
