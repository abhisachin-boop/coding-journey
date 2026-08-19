# Circular Singly Linked List
# The last node points back to the head instead of None.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def display(self):
        if self.head is None:
            print("Empty")
            return

        values = []
        current = self.head
        while True:
            values.append(str(current.data))
            current = current.next
            if current == self.head:
                break

        print(" -> ".join(values) + " -> (head)")


linked_list = CircularLinkedList()
for value in [10, 20, 30, 40]:
    linked_list.append(value)

linked_list.display()
