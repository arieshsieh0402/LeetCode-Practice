def longestCommonPrefix(strs: list[str]) -> str:
    """
    Solution of 14. Longest Common Prefix.
    """
    prefix = strs[0]

    for word in strs:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

    return prefix
