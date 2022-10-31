def get_intersection_node_1(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    visited = set()

    while head_a:
        visited.add(head_a)
        head_a = head_a.next

    while head_b:
        if head_b in visited:
            return head_b
        head_b = head_b.next

    return None


def get_intersection_node_2(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    a, b = head_a, head_b

    while a != b:
        a = a.next if a else head_b
        b = b.next if b else head_a

    return a
