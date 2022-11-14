def min_remove_to_make_valid(s: str) -> str:
    s_list = list(s)
    stack = []

    for i, c in enumerate(s_list):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if not stack:
                s_list[i] = ''
            else:
                stack.pop()

    for i in stack:
        s_list[i] = ''

    return ''.join(s_list)
