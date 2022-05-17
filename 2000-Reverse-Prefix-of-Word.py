# 2000-Reverse-Prefix-of-Word
def reversePrefix(word: str, ch: str) -> str:
    # Reverse the prefix of word segment
    # by using string slice method with indexing syntax.
    for i in range(len(word)):
        if word[i] == ch:
            return word[:i + 1][::-1] + word[i + 1:]
    # If not found the “ch”, return the word.
    return word

# URL:https://leetcode.com/problems/reverse-prefix-of-word/

# ===========Time Complexity(Worst Case Performence)=========== #

# If the index of "ch" is at the last of word or not found,
# the for-loop will iterate the length of word times (n).
# In conclusion, the time complexity in worst case is O(n).
