from string import ascii_lowercase


# Brute-Force
def appeal_sum_brute(s: str) -> int:
    result = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j + 1]
            result += len(set((sub_string)))

    return result


# Brute-Force Improvement
def appeal_sum_brute_imp(s: str) -> int:
    def check_char_appeal(sub_string):
        appeal_char_dict = {char: False for char in ascii_lowercase}
        char_remain = 26

        for char in sub_string:
            if not appeal_char_dict[char]:
                appeal_char_dict[char] = True
                char_remain -= 1
            if char_remain == 0:
                break

        return len([key for key, val in appeal_char_dict.items() if val])

    result = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j + 1]
            result += check_char_appeal(sub_string)

    return result
