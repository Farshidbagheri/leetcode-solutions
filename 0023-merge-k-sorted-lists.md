# 0023 - Merge k Sorted Lists (Hard)

## Problem

You are given an array of **k** linked-lists, where each linked list is sorted in **ascending order**.

Merge all the linked-lists into **one sorted linked list** and return its head.

---

## Examples

### Example 1  
**Input:**  
`lists = [[1,4,5],[1,3,4],[2,6]]`  

**Output:**  
`[1,1,2,3,4,4,5,6]`

**Explanation:**  
The linked lists are:  

**Output:**  

1 -> 4 -> 5
1 -> 3 -> 4
2 -> 6

Merging all lists results in:  


---

### Example 2  
**Input:**  
`lists = []`  
**Output:**  
`[]`

### Example 3  
**Input:**  
`lists = [[]]`  
**Output:**  
`[]`

---

## Intuition

We need to merge **k sorted linked lists** efficiently.

A simple approach would be to gather all values and sort them, but this is inefficient.

A better approach is to always pick the **smallest current node** among the k lists.  
A **min-heap** lets us do this efficiently:

- Put the head node of each non-empty list in the heap.
- Repeatedly pop the smallest element.
- Push that node’s `.next` into the heap.
- Build the final list one node at a time.

This guarantees good performance even when `k` is large.

---

## Algorithm

1. Create an empty min-heap.
2. Push `(node.val, index, node)` for each non-empty list into the heap.
3. Initialize a dummy node and a pointer `current = dummy`.
4. While the heap is not empty:
   - Pop the smallest tuple `(value, idx, node)`.
   - Attach `node` to `current.next` and move `current`.
   - If `node.next` exists, push `(node.next.val, idx, node.next)` back into the heap.
5. Return `dummy.next`.

---

## Complexity

- **Time Complexity:** `O(N log k)`  
  `N = total number of nodes`  
  `k = number of lists`  

- **Space Complexity:** `O(k)` for the heap.

---

## Python Code

```python
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # Min-heap for storing (value, list index, node)
        min_heap: list[tuple[int, int, ListNode]] = []

        # Push the head of each list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode()
        current = dummy

        # Extract nodes in increasing order
        while min_heap:
            value, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next
