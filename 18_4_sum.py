from typing import List


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    answer = []
    n = len(nums)
    nums.sort()

    for a in range(n):
        if a > 0 and nums[a] == nums[a - 1]:
            continue

        for b in range(a + 1, n):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue

            c, d = b + 1, n - 1
            while c < d:
                candidate = [nums[a], nums[b], nums[c], nums[d]]
                curr_sum = sum(candidate)

                if curr_sum > target:
                    d -= 1

                elif curr_sum < target:
                    c += 1

                else:
                    answer.append(candidate)
                    c += 1
                    while c < d and nums[c] == nums[c - 1]:
                        c += 1

    return answer
