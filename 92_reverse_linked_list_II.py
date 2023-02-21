def reverse_between(
    self, head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    # Reverse function
    def reverse(sub_head):
        prev = None
        curr = sub_head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    # Memorize the memory address of head
    dummy = ListNode()
    dummy.next = head

    # Assign dummy node to prev and head to curr since if left is equal to 1,
    # which means the head will reverse too, in this case,
    # the prev will be dummy node, and we will update the dummy.next to new head.
    prev = dummy
    curr = head
    # Find the start point to reverse
    i = 0
    while curr:
        i += 1
        if i == left:
            original_left = prev
            sub_head = curr
        if i == right:
            original_right = curr.next
            curr.next = None # As the ending condition of reverse function loop
            break
        prev = curr
        curr = curr.next

    # Connect the original_left to reversed_head and
    # reversed_tail to original_right
    # Finally return dummy.next
    reversed_head = reverse(sub_head)
    reversed_tail = sub_head
    original_left.next = reversed_head
    reversed_tail.next = original_right
    return dummy.next
