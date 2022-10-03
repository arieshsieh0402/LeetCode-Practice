from collections import Counter


def can_construct_pointer(ransom_note: str, magazine: str) -> bool:
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


def can_construct_collection_counter(ransom_note: str, magazine: str) -> bool:
    ransom_note_count = Counter(ransom_note)
    magazine_count = Counter(magazine)

    return not bool(ransom_note_count - magazine_count)


def can_construct(ransomNote: str, magazine: str) -> bool:
    letter_counter = {}
    for char in magazine:
        if char not in letter_counter:
            letter_counter[char] = 1
        else:
            letter_counter[char] += 1

    for char in ransomNote:
        if char in letter_counter and letter_counter[char] > 0:
            letter_counter[char] -= 1
        else:
            return False
    return True
