# Binary Search Tree: delete a node


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root


def minimum_node(root):
    current = root
    while current.left:
        current = current.left
    return current


def delete(root, target):
    if root is None:
        return None

    if target < root.data:
        root.left = delete(root.left, target)
    elif target > root.data:
        root.right = delete(root.right, target)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        successor = minimum_node(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)

    return root


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


root = None
for value in [10, 5, 15, 2, 7, 12, 20]:
    root = insert(root, value)

print("Before deletion:", inorder(root))
root = delete(root, 15)
print("After deleting 15:", inorder(root))
