def is_isomorphic(s: str, t: str) -> bool:
    compare = {}
    for i in range(len(s)):
        if s[i] not in compare:
            if t[i] in compare.values():
                return False
            compare[s[i]] = t[i]
        else:
            if compare[s[i]] != t[i]:
                return False
    return True
