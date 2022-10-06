def is_happy(n: int) -> bool:
    seen = {}
    while True:
        curr_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            curr_sum += digit ** 2
        if curr_sum in seen:
            return False
        elif curr_sum == 1:
            return True
        else:
            seen[curr_sum] = 1
            n = curr_sum
