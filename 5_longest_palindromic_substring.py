def longest_palindrome(s: str) -> str:
    longest_palindrome = ''

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i: j + 1]
            if substring == substring[::-1]:
                if len(substring) > len(longest_palindrome):
                    longest_palindrome = substring

    return longest_palindrome


def longest_palindrome(s: str) -> str:
    start, max_length = 0, 0

    def find_longest_palindrome(s, left, right):
        nonlocal start
        nonlocal max_length
        while (left >= 0) and (right <= len(s) - 1) and (s[left] == s[right]):
            left -= 1
            right += 1
        if max_length < right - left - 1:
            start = left + 1
            max_length = right - left - 1

    for i in range(len(s) - 1):
        find_longest_palindrome(s=s, left=i, right=i)
        find_longest_palindrome(s=s, left=i, right=i + 1)

    return s[start:start + max_length]


def longest_palindrome(s: str) -> str:
    dp = [[0] * len(s) for _ in range(len(s))]
    longest_palindrome = ''

    for n in range(len(dp)):
        start = 0
        end = n
        while end < len(dp):
            if start > end:
                dp[start][end] = 0
            elif start == end:
                dp[start][end] = 1
            elif end == start + 1:
                dp[start][end] = 2 if s[start] == s[end] else 0
            else:
                if dp[start + 1][end - 1] == 0 or s[start] != s[end]:
                    dp[start][end] = 0
                else:
                    dp[start][end] = dp[start + 1][end - 1] + 2

            if dp[start][end] > len(longest_palindrome):
                longest_palindrome = s[start: end + 1]

            start += 1
            end += 1

    return longest_palindrome
