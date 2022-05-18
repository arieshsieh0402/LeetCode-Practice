def reverse_prefix(word: str, ch: str) -> str:
    """
    Solution of 2000-Reverse-Prefix-of-Word.

    word -- consists of lowercase English letters.
    ch -- is a lowercase English letter.

    """
    # Reverse the prefix of word segment
    # by using string slice method with indexing syntax.
    for key, value in enumerate(word):
        if value == ch:
            return word[:key + 1][::-1] + word[key + 1:]
    # If not found the “ch”, return the word.
    return word

# URL:https://leetcode.com/problems/reverse-prefix-of-word/

# ===========Time Complexity(Worst Case Performence)=========== #

# If the index of "ch" is at the last of word or not found,
# the for-loop will iterate the length of word times (n).
# In conclusion, the time complexity in worst case is O(n).
