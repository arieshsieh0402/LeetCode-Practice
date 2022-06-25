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

