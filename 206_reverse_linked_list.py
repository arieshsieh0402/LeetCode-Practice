class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printList(self):
        show_on_array = []
        temp = self.head
        while temp:
            show_on_array.append(temp.data)
            temp = temp.next
        return show_on_array


lk = LinkedList()

for i in range(1, 6):
    lk.insert_end(i)

print(f"This is original linked list: {lk.printList()}")


lk.reverse_list()
print(f"This is reversed linked list: {lk.printList()}")


# URL:https://leetcode.com/problems/reverse-linked-list/

# Time Complexity
# O(n)

# Space
# O(n) ---> not sure
