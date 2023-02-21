from string import ascii_letters, digits


def is_palindrome(s: str):
    new_s = ''
    for i in range(len(s)):
        if s[i] in ascii_letters or s[i] in digits:
            new_s += s[i]

    new_s = new_s.lower()

    left = 0
    right = len(new_s) - 1

    while left < right:
        if new_s[left] != new_s[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


def is_palindrome_with_isalnum(s):
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
