import math


def min_sub_array_len_brute_force(target, nums):
    min_length = math.inf
    for i in range(len(nums)):
        curr_sum = 0
        curr_length = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            curr_length += 1
            if curr_sum >= target:
                min_length = min(min_length, curr_length)
                break
    return 0 if min_length == math.inf else min_length


def min_sub_array_len_two_pointer(target, nums) -> int:
    min_length = math.inf
    left = 0
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        while curr_sum >= target:
            min_length = min(min_length, i - left + 1)
            curr_sum -= nums[left]
            left += 1
    return min_length if min_length != math.inf else 0
