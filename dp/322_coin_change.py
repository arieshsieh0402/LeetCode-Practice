from collections import deque
import math
from typing import List


def coin_change_dp(coins: List[int], amount: int) -> int:
    dp = [0] + [math.inf for _ in range(amount)]
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[-1] == math.inf:
        return -1
    else:
        return dp[-1]


def coin_change_bfs(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    q = deque()
    q.append(amount)
    visited = set()
    depth = 0
    while q:
        for _ in range(len(q)):
            curr_amount = q.popleft()

            if curr_amount < 0:
                continue
            elif curr_amount == 0:
                return depth
            if curr_amount not in visited:
                visited.add(curr_amount)
                for coin in coins:
                    q.append(curr_amount - coin)
        depth += 1
    return -1
