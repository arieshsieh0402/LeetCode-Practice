from typing import List


def next_greater_elements(nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        element_loops = 0
        has_next_grater = False
        j = i + 1
        while (element_loops <= len(nums) - 1) and (not has_next_grater):
            if j >= len(nums):
                j = 0
            if nums[j] > nums[i]:
                has_next_grater = True
                result.append(nums[j])
                break
            j += 1
            element_loops += 1
        if not has_next_grater:
            result.append(-1)
    return result
