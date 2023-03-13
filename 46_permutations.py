from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    def dfs(depth, visited, path):
        if depth == len(nums):
            permutations.append(path.copy())
            return

        for digit in nums:
            if digit in visited:
                continue
            path.append(digit)
            visited.add(digit)
            dfs(depth + 1, visited, path)
            path.pop()
            visited.remove(digit)

    permutations = []
    dfs(0, set(), [])

    return permutations
