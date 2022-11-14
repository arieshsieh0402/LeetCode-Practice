def longest_nice_substring(s: str) -> str:
    ans = ''
    for i in range(len(s)):
        for j in range(len(s)):
            sub_string = s[i: j + 1]
            sub_string_set = set(sub_string)
            if all(char.swapcase() in sub_string_set for char in sub_string):
                ans = max(ans, sub_string, key=len)
    return ans
