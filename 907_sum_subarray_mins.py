from typing import List


def sum_subarray_mins_brute(arr: List[int]) -> int:
    ans = 0
    n = len(arr)
    for i in range(n):
        smallest = arr[i]
        for j in range(i, n):
            smallest = min(smallest, arr[j])
            ans += smallest

    return ans % (10 ** 9 + 7)


def sum_subarray_mins_expansion(arr: List[int]) -> int:
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
