from typing import List


def mincost_tickets(days: List[int], costs: List[int]) -> int:
    dp = [0 for _ in range(days[-1] + 1)]

    for curr_day in range(days[-1] + 1):
        if curr_day not in days:
            dp[curr_day] = dp[curr_day - 1]
        else:
            dp[curr_day] = min(
                dp[max(0, curr_day - 1)] + costs[0],  # Per one day cost.
                dp[max(0, curr_day - 7)] + costs[1],  # Per 7 days cost.
                dp[max(0, curr_day - 30)] + costs[2]  # Per 30 days cost.
            )
    return dp[-1]
