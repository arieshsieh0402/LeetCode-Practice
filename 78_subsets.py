from typing import List


def subsets(self, nums: List[int]) -> List[List[int]]:
    sub_sets = []
    curr_set = []

    def dfs(i):
        if i >= len(nums):
            sub_sets.append(curr_set.copy())
            return
        curr_set.append(nums[i])
        dfs(i + 1)
        curr_set.pop()
        dfs(i + 1)

    dfs(0)

    return sub_sets
