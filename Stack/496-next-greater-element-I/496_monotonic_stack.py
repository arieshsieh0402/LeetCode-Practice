from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    monotonic_stack = []
    greater_number = {}

    for curr_num in nums2:
        while monotonic_stack and curr_num > monotonic_stack[-1]:
            pop_out_num = monotonic_stack.pop()
            greater_number[pop_out_num] = curr_num

        monotonic_stack.append(curr_num)

    next_greater_element = []

    for num in nums1:
        if num in greater_number:
            next_greater_element.append(greater_number[num])
        else:
            next_greater_element.append(-1)

    return next_greater_element
