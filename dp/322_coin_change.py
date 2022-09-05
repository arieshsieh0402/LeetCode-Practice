from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    dp = [0] + [float('inf') for _ in range(amount)]
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[-1] == float('inf'):
        return -1
    else:
        return dp[-1]
