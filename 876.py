# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def middle_node_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
    length = 0
    dummy_head = head
    while dummy_head:
        length += 1
        dummy_head = dummy_head.next
    execute_next = length // 2

    while execute_next > 0:
        head = head.next
        execute_next -= 1
    return head


def middle_node_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
    nodes = {}
    nodes_length = 1
    while head:
        nodes[nodes_length] = head
        head = head.next
        if not head:
            break
        nodes_length += 1

    return nodes[(nodes_length // 2) + 1]


def middle_node_3(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
