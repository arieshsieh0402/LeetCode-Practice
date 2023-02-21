def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]

    return nums


def merge_sort(nums):
    def merge(arr1, arr2):
        i = 0
        j = 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                result.append(arr2[j])
                j += 1
            else:
                result.append(arr1[i])
                i += 1

        # arr1 or arr2 might have some elements left
        # use loop to put them all into result

        while i < len(arr1):
            result.append(arr1[i])
            i += 1

        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result

    if len(nums) == 1:
        return nums
    else:
        middle = len(nums) // 2
        left_arr = nums[:middle]
        right_arr = nums[middle:len(nums)]
        return merge(merge_sort(left_arr), merge_sort(right_arr))


# Quick sort
def partition(nums, p, r):
    pivot = nums[r]
    i = p - 1
    for j in range(p, r):
        if nums[j] <= pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]

    return i + 1


def quick_sort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        quick_sort(nums, p, q - 1)
        quick_sort(nums, q + 1, r)

# quick_sort(nums, 0, len(nums) - 1)


# Heap Sort
nums = [5, 1, 1, 2, 0, 0]
heap_size = len(nums) - 1


def build_max_heap():
    for i in range(heap_size // 2, -1, -1):
        max_heapify(i)


def max_heapify(i):
    left = 2 * i + 1
    right = 2 * i + 2

    if left <= heap_size and nums[left] > nums[i]:
        largest = left
    else:
        largest = i
    if right <= heap_size and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(largest)


def heap_sort():
    global heap_size
    build_max_heap()
    for i in range(len(nums) - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heap_size -= 1
        max_heapify(0)


heap_sort()
