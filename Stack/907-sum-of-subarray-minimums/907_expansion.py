from typing import List


def sum_subarray_mins(arr: List[int]) -> int:
    result = 0
    for i, num in enumerate(arr):
        left = i - 1
        right = i + 1
        while left >= 0 and arr[left] > num:
            left -= 1

        while right < len(arr) and arr[right] >= num:
            right += 1

        left_length = i - left
        right_length = right - i

        result += (num * (left_length * right_length))

    return result % (10 ** 9 + 7)
