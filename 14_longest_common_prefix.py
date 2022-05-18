def longest_common_prefix(strs: list[str]) -> str:
    """
    Solution of 14. Longest Common Prefix.
    """
    prefix = strs[0]

    for word in strs:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

    return prefix

# URL:https://leetcode.com/problems/longest-common-prefix/

# ===========Time Complexity(Worst Case Performence)=========== #
# O(n^2)

# BTW: This is not my answer.
