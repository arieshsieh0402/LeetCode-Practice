from typing import List


def find_duplicate(nums: List[int]) -> int:
    nums_set = set(nums)

    for i in range(len(nums)):
        if nums[i] in nums_set:
            nums_set.remove(nums[i])
        else:
            return nums[i]


def find_duplicate_bs(nums: List[int]) -> int:
    left = 1
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        counter = 0
        for num in nums:
            if num <= mid:
                counter += 1
        if counter <= mid:
            left = mid + 1
        else:
            right = mid
    return left
