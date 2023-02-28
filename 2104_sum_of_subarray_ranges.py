from typing import List


def sub_array_ranges_brute_1(nums: List[int]) -> int:
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            curr_sub = nums[i: j + 1]
            largest = max(curr_sub)
            smallest = min(curr_sub)
            ans += largest - smallest

    return ans


def sub_array_ranges_brute_2(nums: List[int]) -> int:
    ans = 0
    n = len(nums)
    for i in range(n):
        smallest = largest = nums[i]
        for j in range(i + 1, n):
            smallest = min(smallest, nums[j])
            largest = max(largest, nums[j])
            ans += largest - smallest

    return ans
