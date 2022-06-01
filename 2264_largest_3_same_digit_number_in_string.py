def largest_good_integer(num: str) -> str:
    i = 9
    while i > 0:
        if str(111 * i) in num:
            return str(111 * i)
        i -= 1

    return "000" if "000" in num else ""


# URL:https://leetcode.com/problems/largest-3-same-digit-number-in-string/submissions/

# Time Complexity
# O(n)

# Space
# O(1)
