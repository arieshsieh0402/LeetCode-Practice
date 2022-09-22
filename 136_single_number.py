from typing import List


def single_number_hash_table(nums: List[int]) -> int:
    counter = {}
    for num in nums:
        if num in counter:
            counter.pop(num)
        else:
            counter[num] = 1

    for num in counter.keys():
        return num


def single_number_set(nums: List[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)


def single_number_xor(nums: List[int]) -> int:
    ans = 0
    for num in nums:
        ans ^= num
    return ans
