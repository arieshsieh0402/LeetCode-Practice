def timeRequiredToBuy(tickets, k):
    counter = 0
    target = tickets[k]
    while target > 0:
        for i in range(len(tickets)):
            tickets[i] -= 1
            if tickets[i] >= 0:
                counter += 1
                if tickets[k] == 0:
                    break
        target -= 1
    return counter


# URL: https://leetcode.com/problems/time-needed-to-buy-tickets/

# 1. Set counter to the seconds counter
# 2. Target is the number of tickets that the person needs to buy for ticket[k]
# 3. Set a while loop, run through the entire array, only when ticket[i] is greater than or equal to 0 after minus 1, will counter plus 1
# 4. If ticket[k] is 0, break out of the loop
# 5. After each while loop runs, the target minus 1

# Complexities

# Time: O(n^2)  >>>>>> I'm not sure.
# Space: >>>>>> I haven't learned how to deal with it
