# Doubly Linked List
# Each node points to both the next and previous node.


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        print(" <-> ".join(values) if values else "Empty")

    def display_backward(self):
        if self.head is None:
            print("Empty")
            return

        current = self.head
        while current.next:
            current = current.next

        values = []
        while current:
            values.append(str(current.data))
            current = current.prev
        print(" <-> ".join(values))


linked_list = DoublyLinkedList()
for value in [10, 20, 30, 40]:
    linked_list.append(value)

print("Forward:")
linked_list.display_forward()
print("Backward:")
linked_list.display_backward()
