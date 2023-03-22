from typing import List


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    n = len(nums)

    for i in range(n - 1):
        complement = target - nums[i]
        for j in range(i + 1, n):
            if nums[j] == complement:
                return [i, j]


def two_sum_sort(nums: List[int], target: int) -> List[int]:
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


def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
    nums_dt = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dt:
            return [nums_dt[complement], i]
        nums_dt[num] = i
