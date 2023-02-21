class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.capacity = 1000
        self.hash_table = [None] * self.capacity

    # Calculate the index of the hash table.
    def hash(self, key):
        index = key % self.capacity
        return index

    # Add a new key, value pair into the hash table
    def put(self, key, value):
        # Get the index
        index = self.hash(key)

        # There are three conditions to consider:
        # 1. If there is no key, value pair existing in the index,
        # then create a new node to the index in hash table.
        if self.hash_table[index] is None:
            self.hash_table[index] = Node(key, value)

        # If the key present in the index, then
        else:
            # Initialize the curr_node with the hash index.
            curr_node = self.hash_table[index]

            # Iterate through the loop while there is curr_node
            while curr_node:
                # 2. Check if the curr_node has the same key as the new node,
                # then we update the value and return.
                if curr_node.key == key:
                    curr_node.value = value
                    return
                # 3. If there is different keys with same hash index
                # then we come out of the loop and --->
                if curr_node.next is None:
                    break

                curr_node = curr_node.next

            # ---> add the new node to curr.next node.
            curr_node.next = Node(key, value)

    def get(self, key):
        index = self.hash(key)
        # curr_node is the index of the hash table
        curr_node = self.hash_table[index]

        while curr_node:
            # There are 2 conditions:
            # 1. If the key of the new node is same as the curr_node
            # then return the value
            if curr_node.key == key:
                return curr_node.value
            # 2. If the key is not same then iterate through the list.
            else:
                curr_node = curr_node.next
        # If there is no key present in the hash table as requested, return -1.
        return -1

    def remove(self, key):
        index = self.hash(key)
        curr_node = self.hash_table[index]
        prev_node = curr_node

        if self.hash_table[index] is None:
            return

        # To remove the key there are 3 conditions:
        # 1. if the curr_node key matches with the key
        # then update the hash table index
        if curr_node.key == key:
            self.hash_table[index] = curr_node.next
        else:
            # Update the curr_ node to next
            curr_node = curr_node.next
            while curr_node:
                # 3 If the key is not found, update the node
                # update the pointer of prev to current.next.
                if curr_node.key != key:
                    prev_node = prev_node.next
                    curr_node = curr_node.next
                # 2. If the curr node has the same key,
                # break the condition and come out of the loop or
                # else it will run infinitely.
                else:
                    prev_node.next = curr_node.next
                    break
