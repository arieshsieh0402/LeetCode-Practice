from typing import List


def intersection_set_fun(nums: List[List[int]]) -> List[int]:
    answer_set = set(nums[0])

    for i in range(1, len(nums)):
        answer_set = answer_set.intersection(set(nums[i]))
    return sorted(answer_set)


def intersection_hash_table(nums: List[List[int]]) -> List[int]:
    count = {}

    flatted_nums = sum(nums, [])

    for num in flatted_nums:
        count[num] = count.get(num, 0) + 1

    target_num_count = len(nums)
    result = []

    for key, value in count.items():
        if value == target_num_count:
            result.append(key)
    return sorted(result)
