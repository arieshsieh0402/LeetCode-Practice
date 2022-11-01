def running_sum_1(nums: List[int]) -> List[int]:
    ans = []
    for i in range(len(nums)):
        ans.append(sum(nums[:i + 1]))
    return ans


def running_sum_2(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1, 0, -1):
        nums[i] = sum(nums[:i + 1])
    return nums
