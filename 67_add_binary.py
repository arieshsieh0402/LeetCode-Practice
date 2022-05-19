def add_binary(a: str, b: str) -> str:
    """
    Solution of 67. Add Binary.
    Given two binary strings a and b, return their sum as a binary string.

    a, b -- two binary strings.
    """
    if a == "0" and b == "0":
        return "0"

    a_dec_int = 0
    b_dec_int = 0

    for power, digit in enumerate(reversed(a)):
        a_dec_int += (2 ** power) * int(digit)

    for power, digit in enumerate(reversed(b)):
        b_dec_int += (2 ** power) * int(digit)

    result_dec_int = a_dec_int + b_dec_int
    result_bin_str = ""

    while result_dec_int >= 1:
        result_bin_str += str(result_dec_int % 2)
        result_dec_int = result_dec_int // 2

    return result_bin_str[::-1]

# URL:https://leetcode.com/problems/add-binary/

# ===========Time Complexity(Worst Case Performence)=========== #
# O(n+m)
