# Singly Linked List: insertion at beginning/position and deletion by position


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values) if values else "Empty")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise ValueError("Position cannot be negative")

        if position == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next

        if current is None:
            raise IndexError("Position out of range")

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_at_position(self, position):
        if position < 0 or self.head is None:
            return False

        if position == 0:
            self.head = self.head.next
            return True

        current = self.head
        for _ in range(position - 1):
            if current.next is None:
                return False
            current = current.next

        if current.next is None:
            return False

        current.next = current.next.next
        return True


linked_list = SinglyLinkedList()
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(10)
linked_list.insert_at_position(30, 2)
linked_list.insert_at_position(25, 2)

print("After insertions:")
linked_list.display()

linked_list.delete_at_position(1)
print("After deleting position 1:")
linked_list.display()
