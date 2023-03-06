from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    combinations = []
    n = len(candidates)

    def dfs(i, curr_combin, curr_sum):
        if curr_sum == target:
            combinations.append(curr_combin.copy())
            return
        if i >= n or curr_sum >= target:
            return

        curr_combin.append(candidates[i])
        dfs(i, curr_combin, curr_sum + candidates[i])
        curr_combin.pop()
        dfs(i + 1, curr_combin, curr_sum)

    dfs(0, [], 0)

    return combinations
