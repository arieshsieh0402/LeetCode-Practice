import math
from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    n = len(nums)
    distance = math.inf
    result = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = nums[left] + nums[right] + nums[i]
            if curr_sum == target:
                return curr_sum
            elif curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1

            curr_distance = abs(target - curr_sum)

            if curr_distance < distance:
                distance = curr_distance
                result = curr_sum

    return result
