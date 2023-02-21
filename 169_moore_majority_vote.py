from typing import List


def majority_element(nums: List[int]) -> int:
    vote, majority = 0, None

    for num in nums:
        if vote == 0:
            majority = num
        vote += 1 if majority == num else -1

    return majority

# Time: O(n)
# Space: O(1)
