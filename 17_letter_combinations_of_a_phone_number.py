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
