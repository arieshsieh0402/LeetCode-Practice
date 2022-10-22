def search(nums, target):
    min = 0
    max = len(nums) - 1
    while min <= max:
        middle = (max + min) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            min = middle + 1
        else:
            nums[middle] > target
            max = middle - 1
    return -1
