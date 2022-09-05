from typing import List


def mincost_tickets(days: List[int], costs: List[int]) -> int:
    # Create a dp table to store the cost of each day until last day.
    dp = [0 for _ in range(days[-1] + 1)]

    for current_day in range(days[-1] + 1):
        if current_day not in days:
            # If current day not in travel day, the cost until current
            # day would be the cost of previous day.
            dp[current_day] = dp[current_day - 1]
        else:
            dp[current_day] = min(
                dp[max(0, current_day - 1)] + costs[0],  # Per one day cost.
                dp[max(0, current_day - 7)] + costs[1],  # Per 7 days cost.
                dp[max(0, current_day - 30)] + costs[2]  # Per 30 days cost.
            )

    return dp[-1]
