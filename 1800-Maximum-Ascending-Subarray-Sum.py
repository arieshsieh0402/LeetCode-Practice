def maxAscendingSum(nums: list[int]) -> int:
    """
    Solution of 1800. Maximum Ascending Subarray Sum.

    nums -- an array of positive integers nums.

    """
    if len(nums) == 1:
        return nums[0]
    max_sum = 0
    pointer = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            temp_sum = sum(nums[pointer:i])
            if temp_sum > max_sum:
                max_sum = temp_sum
            pointer = i
        else:
            if i == len(nums) - 1:
                temp_sum = sum(nums[pointer:])
                if temp_sum > max_sum:
                    max_sum = temp_sum
            else:
                continue

    return max_sum


print(maxAscendingSum([10, 20, 30, 5, 10, 50]))

# URL:https://leetcode.com/problems/maximum-ascending-subarray-sum/

# ===========Time Complexity(Worst Case Performence)=========== #
# O(n)
