from typing import List


def rob_brute_force(nums: List[int]) -> int:
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    i = len(nums) - 1
    return max(
        nums[i] + rob_brute_force(nums[:i - 1]), rob_brute_force(nums[:i])
    )


def rob_dp(nums: List[int]) -> int:
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
