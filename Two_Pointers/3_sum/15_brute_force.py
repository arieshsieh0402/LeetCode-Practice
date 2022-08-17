from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = []

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp_ans = sorted([nums[i], nums[j], nums[k]])
                    if temp_ans not in result:
                        result.append(temp_ans)

    return result
