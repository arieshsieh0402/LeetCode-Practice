from typing import List


def max_sub_array(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    max_sum = nums[0]
    cur_sum = 0
    for num in nums:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)
    return max_sum
