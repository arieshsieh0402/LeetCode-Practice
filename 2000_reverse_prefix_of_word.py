def reverse_prefix(word: str, ch: str) -> str:
    for key, value in enumerate(word):
        if value == ch:
            return word[:key + 1][::-1] + word[key + 1:]
    return word


def reverse_prefix_two_pointers(word: str, ch: str) -> str:
    word_list = list(word)
    left = 0
    right = 0

    for i in range(len(word_list)):
        if word_list[i] == ch:
            right = i
            break

    while left <= right:
        word_list[left], word_list[right] = word_list[right], word_list[left]
        left += 1
        right -= 1

    return "".join(word_list)
