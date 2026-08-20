# Binary Tree: level-order traversal and height
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

print("Level order:", level_order(root))
print("Height:", height(root))
