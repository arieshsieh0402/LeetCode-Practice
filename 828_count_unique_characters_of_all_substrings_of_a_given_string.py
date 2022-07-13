# Brute-Force
from collections import Counter


def unique_letter_string_brute(s: str) -> int:
    def count_unique_chars(s: str) -> int:
        unique_chars_dict = Counter(s)
        return len([key for key, val in unique_chars_dict.items() if val == 1])

    unique_char_dict = {}
    length_count = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j + 1]
            if sub_string not in unique_char_dict:
                unique_char_dict[sub_string] = count_unique_chars(sub_string)
            length_count += unique_char_dict[sub_string]

    return length_count
