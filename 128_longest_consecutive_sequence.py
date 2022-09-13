def longest_consecutive(nums):
    hash_table = {}
    longest_length = 0

    for num in nums:
        if num not in hash_table:
            hash_table[num] = num

    for num in list(hash_table.keys()):
        next = num + 1
        prev = num - 1
        hash_table.pop(num)
        while next in hash_table:
            next += 1
        while prev in hash_table:
            prev -= 1
        longest_length = max(longest_length, next - prev - 1)

    return longest_length
