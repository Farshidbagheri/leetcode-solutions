# 0024 - Swap Nodes in Pairs (Medium)

## Problem

Given the **head** of a singly linked list, swap every two adjacent nodes and return the head.

You **must not modify** the values in the list’s nodes — only the **node pointers** may be changed.

---

## Examples

### Example 1
**Input:**  
`head = [1,2,3,4]`  
**Output:**  
`[2,1,4,3]`

### Example 2
**Input:**  
`head = []`  
**Output:**  
`[]`

### Example 3
**Input:**  
`head = [1]`  
**Output:**  
`[1]`

---

## Intuition

We want to swap nodes in pairs without changing node values.  
For a pair:


prev -> first -> second -> next_pair


After swapping:

prev -> second -> first -> next_pair


To handle the head smoothly, we use a **dummy node** whose `next` points to the original head.

The process repeats until all possible adjacent pairs are swapped.

---

## Algorithm

1. Create a dummy node and set `dummy.next = head`.  
2. Set two pointers:
   - `prev = dummy`
   - `head` (current position in the list)
3. While at least two nodes remain (`head` and `head.next` exist):
   - Assign:
     - `first = head`
     - `second = head.next`
   - Rewire links:
     - `prev.next = second`
     - `first.next = second.next`
     - `second.next = first`
   - Move pointers:
     - `prev = first`
     - `head = first.next`
4. Return `dummy.next` as the new head.

---

## Complexity

- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(1)` — constant extra space

---

## Python Code

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap every two adjacent nodes in a singly linked list.
        Node values must not be modified; only pointers are changed.
        """
        dummy = ListNode(0, head)
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Connect previous node to second
            prev.next = second
            # Link first to the node after the pair
            first.next = second.next
            # Second now points back to first
            second.next = first

            # Move pointers forward
            prev = first
            head = first.next

        return dummy.next


