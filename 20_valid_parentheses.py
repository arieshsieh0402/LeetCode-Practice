def is_valid(s: str) -> bool:
    # The parentheses must be in pairs.
    if len(s) % 2 == 1:
        return False

    stack = []
    dict_paren = {")": "(",
                  "]": "[",
                  "}": "{"
                  }

    for char in s:
        if char in dict_paren.values():
            stack.append(char)
        else:
            # When right parentheses appears,
            # but there is no element for pairing in the stack,
            # return False
            if len(stack) == 0:
                return False
            # If it can be paired, remove the top element of stack by pop()
            # or return False
            elif stack[-1] != dict_paren[char]:
                return False
            stack.pop()
    # If every parentheses can be paired, the length of stack should be 0.
    return len(stack) == 0

# URL:https://leetcode.com/problems/valid-parentheses/submissions/

# ===========Time Complexity(Worst Case Performence)=========== #
# O(n)
