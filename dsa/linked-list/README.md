# Linked List

A linked list stores data in **nodes**. Each node contains:

1. `data` — the value.
2. `next` — a reference to the next node.

## Singly Linked List

```text
10 → 20 → 30 → 40 → None
```

### Core operations

- **Traversal:** visit nodes one by one — O(n)
- **Search:** find a value — O(n)
- **Append:** O(n) in this implementation because we walk to the tail
- **Delete:** O(n)
- **Reverse:** O(n)

## Key idea

Unlike an array, linked-list elements do not need to be stored next to each other in memory. The `next` reference connects one node to another.

## Practice

Try changing `01_singly_linked_list.py` to add:

- insert at the beginning
- insert at a specific position
- delete by position
- count the nodes
