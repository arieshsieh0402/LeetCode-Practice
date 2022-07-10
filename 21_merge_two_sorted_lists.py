# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_two_lists(
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        head = ListNode(None)
        current_node = head

        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = list1.val
                list1 = list1.next
            else:
                current_node.next = list2.val
                list2 = list2.next
            current_node = current_node.next

        if list1:
            current_node.next = list1

        if list2:
            current_node.next = list2

        return head.next
