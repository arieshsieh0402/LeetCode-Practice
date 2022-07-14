# Brute-Force
from collections import Counter


def unique_letter_string_brute(s: str) -> int:
    def count_unique_chars(s: str) -> int:
        unique_chars_dict = Counter(s)
        return len([key for key, val in unique_chars_dict.items() if val == 1])

    unique_char_dict = {}
    result = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j + 1]
            if sub_string not in unique_char_dict:
                unique_char_dict[sub_string] = count_unique_chars(sub_string)
            result += unique_char_dict[sub_string]

    return result


# Expansion

def unique_letter_string_expansion(s: str) -> int:
    result = 0

    for index, char in enumerate(s):
        left = index - 1
        right = index + 1

        while left >= 0 and s[left] != char:
            left -= 1

        while right < len(s) and s[right] != char:
            right += 1

        left_length = index - left
        right_length = right - index

        result += left_length * right_length

    return result
