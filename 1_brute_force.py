from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    n = len(nums)

    for i in range(n - 1):
        complement = target - nums[i]
        for j in range(i + 1, n):
            if nums[j] == complement:
                return [i, j]
