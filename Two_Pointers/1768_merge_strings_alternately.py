def merge_alternately(word1: str, word2: str) -> str:
    result = ''
    length_word1 = len(word1)
    length_word2 = len(word2)
    i = 0
    j = 0

    while i < length_word1 and j < length_word2:
        result += (word1[i])
        result += (word2[j])

        i += 1
        j += 1

    if i == length_word1:
        while j < length_word2:
            result += (word2[j])

            j += 1

    elif j == length_word2:
        while i < length_word1:
            result += (word1[i])

            i += 1

    return result
