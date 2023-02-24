from typing import List


def four_sum_4_loops(nums: List[int], target: int) -> List[List[int]]:
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


def four_sum_k_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    answer = []

    def k_sum(k, start, target, path):
        if k == 2:
            left, right = start, len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    answer.append(path + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif two_sum < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                k_sum(k - 1, i + 1, target - nums[i], path + [nums[i]])

    k_sum(4, 0, target, [])

    return answer
