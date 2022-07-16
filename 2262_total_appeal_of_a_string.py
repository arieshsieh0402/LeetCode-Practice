# Brute-Force
def appeal_sum(s: str) -> int:
    appeal_char_dict = {}
    result = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j + 1]
            if sub_string not in appeal_char_dict:
                appeal_char_dict[sub_string] = len(set((sub_string)))
            result += appeal_char_dict[sub_string]

    return result
