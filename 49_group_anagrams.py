from collections import defaultdict
from typing import List


def group_anagrams_sort(strs: List[str]) -> List[List[str]]:
    anagram_dict = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)

    return list(anagram_dict.values())


def group_anagrams_counter(strs: List[str]) -> List[List[str]]:
    anagram_dict = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1

        anagram_dict[tuple(count)].append(word)

    return list(anagram_dict.values())
