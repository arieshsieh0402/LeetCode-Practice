from typing import List


# Brute-Force
def sum_subarray_mins(arr: List[int]) -> int:
    result = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub_arr = arr[i:j + 1]
            result += min(sub_arr)
    return result

