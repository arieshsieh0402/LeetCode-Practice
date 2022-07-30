from typing import List


def next_greater_elements(nums: List[int]) -> List[int]:
    n = len(nums)
    decrease_stack = []
    result = [-1 for _ in range(n)]

    for i in range(n * 2):
        i = i % n
        while decrease_stack and nums[i] > nums[decrease_stack[-1]]:
            idx = decrease_stack.pop()
            result[idx] = nums[i]

        decrease_stack.append(i)

    return result
