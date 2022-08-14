from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    count = {}

    for n in nums:
        if n not in count:
            count[n] = 1
        else:
            return True

    return False
