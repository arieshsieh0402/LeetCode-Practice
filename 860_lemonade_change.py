from typing import List


def lemonade_change(bills: List[int]) -> bool:
    """
    Solution of 860. Lemonade Change.
    """
    five, ten = 0, 0
    for pay in bills:
        if pay == 5:
            five += 1
        elif pay == 10:
            five, ten = five - 1, ten + 1
        # If pay == 20, the fisrt best option is 
        # give one ten and one five as change.
        elif ten > 0:
            five, ten = five - 1, ten - 1
        else:
            five -= 3
        if five < 0:
            return False
    return True

# URL:https://leetcode.com/problems/lemonade-change/

# Time Complexity
# O(n)

# Space
# O(1)
