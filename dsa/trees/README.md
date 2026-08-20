# Trees

A tree is a hierarchical data structure made of nodes.

## Binary Tree

Each node can have at most two children:
- left child
- right child

```text
        10
       /  \
      5    15
     / \     \
    2   7     20
```

## Traversals

- **Preorder:** Root → Left → Right
- **Inorder:** Left → Root → Right
- **Postorder:** Left → Right → Root
- **Level order:** level by level using a queue

For a Binary Search Tree (BST), inorder traversal produces values in sorted order.
