def backspace_compare_stack(s: str, t: str) -> bool:
    stack_s, stack_c = [], []

    for c in s:
        if stack_s and c == '#':
            stack_s.pop()
        elif c != '#':
            stack_s.append(c)

    for c in t:
        if stack_c and c == '#':
            stack_c.pop()
        elif c != '#':
            stack_c.append(c)

    return stack_s == stack_c


def backspace_compare_two_pointer(s: str, t: str) -> bool:
    i, j = len(s) - 1, len(t) - 1
    s_skip, t_skip = 0, 0
    while i >= 0 or j >= 0:
        while i >= 0:
            if s[i] == '#':
                s_skip += 1
                i -= 1
            elif s_skip > 0:
                s_skip -= 1
                i -= 1
            else:
                break
        while j >= 0:
            if t[j] == '#':
                t_skip += 1
                j -= 1
            elif t_skip > 0:
                t_skip -= 1
                j -= 1
            else:
                break
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False
        if (i >= 0) != (j >= 0):
            return False
        i -= 1
        j -= 1
    return True
