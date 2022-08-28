def letter_combinations(digits: str):
    if not digits:
        return []

    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    all_combinations = ['']

    for digit in digits:
        curr_combinations = []
        for letter in digit_map[digit]:
            for combination in all_combinations:
                curr_combinations.append(combination + letter)
        all_combinations = curr_combinations

    return all_combinations


def letter_combinations_dfs(digits: str):
    if not digits:
        return []

    table = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    ans = []

    def backtrack(i, curr):
        if len(curr) == len(digits):
            ans.append(''.join(list(curr)))
            return
        else:
            for val in table[digits[i]]:
                curr.append(val)
                backtrack(i+1, curr)
                curr.pop()

    backtrack(0, [])

    return ans
