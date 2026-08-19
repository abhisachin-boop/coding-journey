# Common linked-list interview/exam problems


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def build_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def find_length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None


def has_cycle(head):
    # Floyd's slow/fast pointer algorithm
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


head = build_list([10, 20, 30, 40, 50])
print("Length:", find_length(head))
print("Middle:", find_middle(head))
print("Has cycle:", has_cycle(head))
