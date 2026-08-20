# Binary Search Tree (BST): insert, search and inorder traversal


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


def search(root, target):
    if root is None or root.data == target:
        return root is not None

    if target < root.data:
        return search(root.left, target)
    return search(root.right, target)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


root = None
for value in [10, 5, 15, 2, 7, 12, 20]:
    root = insert(root, value)

print("Inorder:", inorder(root))
print("Search 12:", search(root, 12))
print("Search 99:", search(root, 99))
