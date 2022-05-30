from typing import List


def intersection(nums: List[List[int]]) -> List[int]:
    """
    Solution of 2248. Intersection of Multiple Arrays
    """
    answer_set = set(nums[0])
    for i in range(1, len(nums)):
        answer_set = answer_set.intersection(set(nums[i]))
    return sorted(answer_set)

# URL: https://leetcode.com/problems/intersection-of-multiple-arrays/

# ===========Time Complexity(Worst Case Performence)=========== #

# O(n)
