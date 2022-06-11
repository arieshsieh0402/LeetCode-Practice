from typing import List


def singleNumber(nums: List[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)


# URL:https://leetcode.com/problems/single-number/

# Time Complexity
# O(n)

# Space
# O(1)
