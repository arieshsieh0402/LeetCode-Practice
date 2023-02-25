from typing import List


def remove_duplicates_1(nums: List[int]) -> int:
    next_distinct = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[next_distinct] = nums[i]
            next_distinct += 1

    return next_distinct


def remove_duplicates_2(nums: List[int]) -> int:
    duplicates = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            duplicates += 1
        else:
            nums[i - duplicates] = nums[i]

    return len(nums) - duplicates


def remove_duplicates_3(nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
        if n == 2 and nums[0] == nums[1]:
            return 1
        else:
            return n

    curr = nums[0]
    left = right = 1

    while right < n:
        if nums[right] != curr:
            curr = nums[right]
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
        right += 1

    return left
