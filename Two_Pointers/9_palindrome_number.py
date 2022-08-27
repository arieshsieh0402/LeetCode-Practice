def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    temp_x = x
    reverse_x = 0

    while x > 0:
        reverse_x = reverse_x * 10 + x % 10
        x = x // 10

    return reverse_x == temp_x
