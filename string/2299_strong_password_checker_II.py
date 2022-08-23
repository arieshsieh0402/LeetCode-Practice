def strong_password_checker_2(password: str) -> bool:
    n = len(password)
    if n < 8:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_char = '!@#$%^&*()-+'

    for i in range(n):
        if i != 0 and password[i] == password[i - 1]:
            return False
        if password[i].islower():
            has_lower = True
        elif password[i].isupper():
            has_upper = True
        elif password[i].isdigit():
            has_digit = True
        elif password[i] in special_char:
            has_special = True

    return has_lower and has_upper and has_digit and has_special
