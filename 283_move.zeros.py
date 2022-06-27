from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_p = 0

    for forward_p in range(len(nums)):
        if nums[forward_p] != 0 and nums[zero_p] == 0:
            nums[zero_p], nums[forward_p] = nums[forward_p], nums[zero_p]

        if nums[zero_p] != 0:
            zero_p += 1
