# 2000-Reverse-Prefix-of-Word
def reversePrefix(word: str, ch: str) -> str:
    # Check if length of word is 1, return the word.
    if len(word) == 1:
        return word
    # f not, use for-loop to iterate the word,
    # if found “ch”, slice the word to left_segment and right_segment.
    for i in range(len(word)):
        if word[i] == ch:
            left_segment = word[:i + 1]
            # Reverse the left_segment
            # by using string slice method with indexing syntax.
            rv_left_segment = left_segment[::-1]
            right_segment = word[i + 1:len(word)]
            # Reverse the left_segment by using string slice method
            # with indexing syntax.
            return rv_left_segment + right_segment
    # If not found the “ch”, return the word.
    return word

# URL:https://leetcode.com/problems/reverse-prefix-of-word/

# ===========Time Complexity(Worst Case Performence)=========== #

# If the index of "ch" is at the last of word or not found,
# the for-loop will iterate the length of word times (n).
# In conclusion, the time complexity in worst case is O(n).
