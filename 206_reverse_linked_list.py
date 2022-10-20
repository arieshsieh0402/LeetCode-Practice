# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None
#         self.num_of_nodes = 0

#     def insert_start(self, data):
#         self.num_of_nodes += 1
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     def insert_end(self, data):
#         self.num_of_nodes += 1
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next is not None:
#                 current_node = current_node.next

#             current_node.next = new_node

#     def printList(self):
#         show_on_array = []
#         temp = self.head
#         while temp:
#             show_on_array.append(temp.data)
#             temp = temp.next
#         return show_on_array


# lk = LinkedList()

# for i in range(1, 6):
#     lk.insert_end(i)

# print(f"This is original linked list: {lk.printList()}")


# lk.reverse_list()
# print(f"This is reversed linked list: {lk.printList()}")


# Iteratively
def reverse_list_iter(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# Recursively
def reverse_list_recur(self, head):
    def reverse(node, prev):
        if not node:
            return prev
        next_node = node.next
        node.next = prev
        return reverse(next_node, node)
    return reverse(head, None)
