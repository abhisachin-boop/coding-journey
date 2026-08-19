# Singly Linked List: create, traverse, search, insert and delete


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
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

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values) if values else "Empty")

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

    def delete(self, target):
        if self.head is None:
            return False

        if self.head.data == target:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


linked_list = SinglyLinkedList()
for value in [10, 20, 30, 40]:
    linked_list.append(value)

print("Original:")
linked_list.display()
print("Index of 30:", linked_list.search(30))

linked_list.delete(20)
print("After deleting 20:")
linked_list.display()

linked_list.reverse()
print("After reversing:")
linked_list.display()
