import math


def maxProfit(prices):
    hold_stock = math.inf
    total_profit = 0

    for curr_price in prices:
        if curr_price < hold_stock:
            hold_stock = curr_price
        else:
            total_profit += curr_price - hold_stock
            hold_stock = curr_price

    return total_profit
