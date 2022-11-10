from itertools import product
from typing import List


def generateParenthesis(n: int) -> List[str]:
    all_pairs = [''.join(i) for i in product('()', repeat=n * 2)]
    result = []

    for pair in all_pairs:
        balance = 0
        for i in range(n * 2):
            if pair[i] == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                break
        if balance == 0:
            result.append(pair)
    return result
