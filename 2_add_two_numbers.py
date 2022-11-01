# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_number, l2_number = [], []
        while l1:
            l1_number.append(l1.val)
            l1 = l1.next
        while l2:
            l2_number.append(l2.val)
            l2 = l2.next

        l1_sum = l2_sum = 0
        for i in range(len(l1_number)):
            l1_sum += l1_number[i] * (10 ** i)
        for i in range(len(l2_number)):
            l2_sum += l2_number[i] * (10 ** i)
        result = str(l1_sum + l2_sum)

        head = ListNode(result[-1])
        dummy = ListNode()
        dummy.next = head
        for i in range(len(result) - 2, -1, -1):
            curr = ListNode(result[i])
            head.next = curr
            head = curr
        return dummy.next
