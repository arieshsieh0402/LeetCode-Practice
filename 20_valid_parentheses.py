def is_valid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False
    stack = []
    bracket_pair = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in bracket_pair.values():
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] != bracket_pair[char]:
                return False
            stack.pop()
    return len(stack) == 0
