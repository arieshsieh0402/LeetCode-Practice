from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    for num1 in nums1:
        for i in range(len(nums2)):
            if nums2[i] == num1:
                j, temp = i + 1, -1
                while j <= len(nums2) - 1:
                    if nums2[j] > num1:
                        temp = nums2[j]
                        result.append(nums2[j])
                        break
                    j += 1
                if temp == -1:
                    result.append(temp)
    return result
