def word_pattern(pattern: str, s: str) -> bool:
    s = s.split()
    if len(pattern) != len(s):
        return False
    mapping = {}
    for i in range(len(pattern)):
        if pattern[i] not in mapping:
            if s[i] not in mapping.values():
                mapping[pattern[i]] = s[i]
            else:
                return False
        elif pattern[i] in mapping:
            if mapping[pattern[i]] != s[i]:
                return False
    return True
