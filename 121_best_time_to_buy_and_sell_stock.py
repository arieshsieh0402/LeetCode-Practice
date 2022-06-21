from typing import List


# Brute-force
def max_profit(prices: List[int]) -> int:
    highest_profit = 0
    for buy in range(len(prices) - 1):
        for sell in range(buy + 1, len(prices)):
            if prices[sell] - prices[buy] > highest_profit:
                highest_profit = prices[sell] - prices[buy]
    return highest_profit if highest_profit > 0 else 0

# The sell day must be after the buy day, so set a left pointer as “buy”
# and right pointer as “sell”. The buy pointer start from first element of
# array and end on second to last. The sell pointer start always start from
# next to buy pointer and end on the last element of array.
# Now, Loop through the array and find the subtractions for all pairs.
# If prices[sell] - prices[buy] > highest_profit, assign to it.
# Final, return the highest_profit if it's grater than 0 or just return 0.

# Time Complexity: O(n^2)
# Nested loop in array of prices.

# Space Complexity: O(1)
# The amount of memory is constant.

#=====================================#

# Improve brute-force
def max_profit(prices: List[int]) -> int:
    buy = 0
    sell = 1
    highest_profit = 0
    while sell < len(prices):
        if prices[sell] > prices[buy]:
            current_profit = prices[sell] - prices[buy]
            highest_profit = max(highest_profit, current_profit)
        else:
            buy = sell
        sell += 1
    return highest_profit

# 1. possible pairs in array.

# 2. Therefore we still set the left and right pointers as buy and sell .
# The buy pointer start from 0 and sell pointer start from next to buy.

# 3. In a while loop, if prices[sell] > prices[buy],
# store the subtractions into current_profit and compare it with
# the highest_profit by max() function.

# 4. If prices[sell] < prices[buy], move the buy pointer to the position of
# sell then move the sell pointer next to buy pointer.

# 5. In the end, return the value of highest_profit.


#=====================================#

# Dynamic Programming
def max_profit(prices: List[int]) -> int:
    dp = [0] * len(prices)
    min_price = prices[0]

    for i in range(len(prices)):
        dp[i] = max(dp[i - 1], prices[i] - min_price)
        min_price = min(min_price, prices[i])
    
    return dp[-1]



