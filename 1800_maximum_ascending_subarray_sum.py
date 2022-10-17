def max_ascending_sum_1(nums):
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


def max_ascending_sum_2(nums):
    if len(nums) == 1:
        return nums[0]
    curr_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        else:
            curr_sum = nums[i]
    return max_sum


def max_ascending_sum_3(nums):
    '''
    Return list version
    '''

    if len(nums) == 1:
        return nums[0]

    curr_sum = max_sum = nums[0]
    head = 0
    end = None
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
                end = i + 1
        else:
            curr_sum = nums[i]
            head = i
    return nums[head:end]
