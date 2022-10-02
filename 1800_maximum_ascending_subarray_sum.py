def max_ascending_sum(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    max_sum = 0
    head = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            curr_sum = sum(nums[head:i])
            max_sum = max(max_sum, curr_sum)
            head = i
        else:
            if i == len(nums) - 1:
                curr_sum = sum(nums[head:])
                max_sum = max(max_sum, curr_sum)
            else:
                continue
    return max_sum
