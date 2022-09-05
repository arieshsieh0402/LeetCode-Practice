from typing import List


# Solution 1
# Recursion

# Find the base case
# Assume the function to find max looted values is rob(i).
# When you face the house_(i), you have two choice, rob or not.
# If you rob, this means that the house you grabbed last time won't be
# house_(i - 1) , because you can't grab an adjacent house.
# In this case,
# the value you looted until house_(i) is nums[i] plus rob(i - 2).
# Otherwise, if you don't rob the house_(i), that means the the value
# you have looted will be rob(i - 1).

def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    i = len(nums) - 1
    return max(nums[i] + rob(nums[:i - 1]), rob(nums[:i]))

# Time Complexity: O(?)
# Space Complexity: O(?)


# Solution 2
# Dynamic Programming
# Use a dynamic programming table dp to store the looted values

def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]

    dp = [None] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[-1]

# Time Complexity: O(n)
# Space Complexity: O(n) 
