from typing import List


def sub_array_ranges(nums: List[int]) -> int:
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            curr_sub = nums[i: j + 1]
            largest = max(curr_sub)
            smallest = min(curr_sub)
            ans += largest - smallest

    return ans
