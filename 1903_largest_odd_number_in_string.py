def largest_odd_number(num: str) -> str:
    """
    Solution of 1903. Largest Odd Number in String.
    """
    i = len(num) - 1
    while i >= 0:
        if int(num[i]) % 2:
            return num[:i + 1]
        i -= 1

    return ""

# URL:https://leetcode.com/problems/largest-odd-number-in-string/

# ===========Time Complexity(Worst Case Performence)=========== #
# O(n)
