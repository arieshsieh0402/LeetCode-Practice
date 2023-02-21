from typing import List


def majority_element(nums: List[int]) -> int:
    n = len(nums)
    count = {}

    if n < 2:
        return nums[0]

    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > n // 2:
            return num

# Time: O(n)
# Space: O(n)
