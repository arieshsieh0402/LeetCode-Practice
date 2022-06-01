from typing import List


def count_consistent_strings(allowed: str, words: List[str]) -> int:
    count = 0
    for i in words:
        if not set(i).difference(set(allowed)):
            count += 1
    return count


# URL:https://leetcode.com/problems/lemonade-change/

# Time Complexity
# O(n)

# Space
# O(1)
