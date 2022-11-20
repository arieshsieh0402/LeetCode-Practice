from typing import List


def partition(s: str) -> List[List[str]]:
    result = []
    part = []

    def dfs(i):
        if i >= len(s):
            result.append(part.copy())
            return
        for j in range(i, len(s)):
            if is_palindrome(s, i, j):
                part.append(s[i:j + 1])
                dfs(j + 1)
                part.pop()
    dfs(0)
    return result


def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
