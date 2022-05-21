def length_of_last_Word(s: str) -> int:
    s_split_list = s.split()
    return len(s_split_list[-1])


# URL:https://leetcode.com/problems/length-of-last-word/

# ===========Time Complexity(Worst Case Performence)=========== #
#
# The split() function in Python's source code that
# runs different loops depending on the properties.
#
# The function will look at each character
# in the string
#
# The inner most loops will run n times for a string of size n.
#
# Therefore, the Time complexity is O(n)
#
# O(n)
