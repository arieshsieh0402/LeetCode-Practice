from string import ascii_lowercase


# Brute-Force
def appeal_sum_brute(s: str) -> int:
    appeal_char_dict = {}
    result = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j + 1]
            if sub_string not in appeal_char_dict:
                appeal_char_dict[sub_string] = len(set((sub_string)))
            result += appeal_char_dict[sub_string]

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
    sub_char_dict = {}

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j + 1]
            if sub_string not in sub_char_dict:
                sub_char_dict[sub_string] = check_char_appeal(sub_string)
            result += sub_char_dict[sub_string]

    return result
