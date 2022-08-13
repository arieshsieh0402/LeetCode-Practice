def backspace_compare(s: str, t: str) -> bool:
    stack_s, stack_t = [], []

    for char in s:
        if not stack_s and char != '#':
            stack_s.append(char)
        elif stack_s and char == '#':
            stack_s.pop()
        elif char != '#':
            stack_s.append(char)

    for char in t:
        if not stack_t and char != '#':
            stack_t.append(char)
        elif stack_t and char == '#':
            stack_t.pop()
        elif char != '#':
            stack_t.append(char)

    return True if stack_s == stack_t else False

# Time: O(n)
# Space: O(n)
