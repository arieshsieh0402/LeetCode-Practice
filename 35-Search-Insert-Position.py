def searchInsert(nums: list[int], target: int) -> int:
    # Binary Search
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if target > nums[mid]:
        return mid + 1
    else:
        return mid

# URL:https://leetcode.com/problems/search-insert-position/    
    
# **Steps**

# 1. Using binary search to find the target in list.
# 2. If found, return the index of target.
# 3. If not found, compare the last nums[mid],
#    if it is greater than target, then index + 1.
# 4. If it is smaller, because the list is to be inserted,
#    return the index of the mid.

# **Complexities**

# - Time: O(logn)
# - Space:
