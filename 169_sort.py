from typing import List


def majority_element(nums: List[int]) -> int:
    if len(nums) < 2:
        return nums[0]

    nums.sort()

    return nums[len(nums) // 2]

# Time: O(nlogn)
# Space: O(1)
