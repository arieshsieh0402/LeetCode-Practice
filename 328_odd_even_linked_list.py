# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    odd_node = head
    even_node = head.next
    even_list_head = even_node

    while even_node and even_node.next:
        odd_node.next = even_node.next
        odd_node = odd_node.next
        even_node.next = even_node.next.next
        even_node = even_node.next

    odd_node.next = even_list_head

    return head
