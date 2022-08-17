from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    if nums[0] > 0:
        return []
    n, result = len(nums), []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum > 0:
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result
