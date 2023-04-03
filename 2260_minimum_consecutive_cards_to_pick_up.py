from collections import defaultdict
import math
from typing import List


def minimum_card_pickup_brute_force(cards: List[int]) -> int:
    min_picked = math.inf

    for left in range(len(cards) - 1):
        for right in range(left + 1, len(cards)):
            if cards[left] == cards[right]:
                min_picked = min(min_picked, right - left + 1)
                break

    return -1 if min_picked == math.inf else min_picked


def minimum_card_pickup_sliding_window(cards: List[int]) -> int:
    left = 0
    counter = defaultdict(int)
    min_picked = math.inf

    for right in range(len(cards)):
        counter[cards[right]] += 1
        while counter[cards[right]] == 2:
            min_picked = min(min_picked, right - left + 1)
            counter[cards[left]] -= 1
            left += 1

    return min_picked if min_picked != math.inf else -1
