def max_ascending_sum(nums: list[int]) -> int:
    """
    Solution of 1800. Maximum Ascending Subarray Sum.

    nums -- an array of positive integers nums.

    """
    max_sum = nums[0]
    left = 0
    right = 1
    while right <= len(nums) - 1:
        if nums[right] > nums[right - 1]:
            temp_sum = sum(nums[left:right + 1])
            if temp_sum > max_sum:
                max_sum = temp_sum
            right += 1
        else:
            left = right
            right += 1
    return max_sum

    # for right in range(1, len(nums)):
    #     if nums[i] <= nums[i - 1]:
    #         temp_sum = sum(nums[pointer:i])
    #         if temp_sum > max_sum:
    #             max_sum = temp_sum
    #         pointer = i
    #     else:
    #         if i == len(nums) - 1:
    #             temp_sum = sum(nums[pointer:])
    #             if temp_sum > max_sum:
    #                 max_sum = temp_sum
    #         else:
    #             continue

    return max_sum

# URL:https://leetcode.com/problems/maximum-ascending-subarray-sum/

# ===========Time Complexity(Worst Case Performence)=========== #
# O(n)
