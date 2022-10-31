from collections import Counter


def sort_colors_2(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0
    right = len(nums) - 1
    curr = 0

    while curr <= right:
        if nums[curr] == 0:
            nums[curr], nums[left] = nums[left], nums[curr]
            left += 1
        elif nums[curr] == 2:
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1
            curr -= 1
        curr += 1


def sort_colors_1(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    counter = Counter(nums)

    curr = 0
    for i in range(3):
        for _ in range(counter[i]):
            nums[curr] = i
            curr += 1
