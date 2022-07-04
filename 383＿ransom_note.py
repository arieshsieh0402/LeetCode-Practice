from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    Given two strings ransomNote and magazine, return true if
    ransomNote can be constructed from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.
    """
    # Set pointer of ransom note
    pointer = 0

    # Turn magazine into list
    magazine_lst = list(magazine)

    while pointer < len(ransom_note):
        try:
            magazine_lst.remove(ransom_note[pointer])
            pointer += 1
        except ValueError:
            return False

    return True

# URL:https://leetcode.com/problems/ransom-note/submissions/

# ===========Time Complexity(Worst Case Performence)=========== #

# 1.The time complexity of turn magazine into list is O(n)
# 2.The time complexity of this while-loop is O(n * m).
# (ransom_note runs n times, magazine_lst.remove() runs m times.)

# Time Complexity is O(n * m) (O(n + n * m) = O(n * m))


def can_construct_collection_counter(ransom_note: str, magazine: str) -> bool:
    ransom_note_count = Counter(ransom_note)
    magazine_count = Counter(magazine)

    return not bool(ransom_note_count - magazine_count)
