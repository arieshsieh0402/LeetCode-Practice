def count_binary_substrings(s: str) -> int:
    prev_len = 0
    curr_len = 1
    count = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr_len += 1
        else:
            prev_len = curr_len
            curr_len = 1
        if prev_len >= curr_len:
            count += 1

    return count
