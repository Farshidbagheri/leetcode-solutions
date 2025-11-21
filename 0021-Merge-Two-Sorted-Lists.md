# 0021 - Merge Two Sorted Lists (Easy)

## Problem

You are given the heads of two **sorted** singly linked lists `list1` and `list2`.

Merge the two lists into **one sorted list**.  
The new list should be made by **splicing together the nodes of the original lists**.  
Return the **head** of the merged linked list.

---

## Examples

**Example 1**

Input:  
`list1 = [1,2,4]`, `list2 = [1,3,4]`  
Output:  
`[1,1,2,3,4,4]`

**Example 2**

Input:  
`list1 = []`, `list2 = []`  
Output:  
`[]`

**Example 3**

Input:  
`list1 = []`, `list2 = [0]`  
Output:  
`[0]`

---

## Intuition

Both lists are already sorted.  
We can walk through them **like the merge step of merge sort**:

- Always take the smaller current node from the two lists.
- Attach it to the tail of the result list.
- Move forward in the list from which we took the node.

To simplify handling of the head, we use a **dummy node** whose `next` will eventually point to the real head of the merged list.

---

## Algorithm

1. Create a dummy node `dummy` and a pointer `tail = dummy`.
2. While both `list1` and `list2` are non-null:
   - If `list1.val <= list2.val`:
     - Set `tail.next = list1` and move `list1 = list1.next`.
   - Else:
     - Set `tail.next = list2` and move `list2 = list2.next`.
   - Move `tail = tail.next`.
3. After the loop, **at most one** of the lists is non-empty.
   - Attach the remaining part with  
     `tail.next = list1 if list1 else list2`.
4. Return `dummy.next` as the head of the merged list.

---

## Complexity

- **Time:** `O(n + m)`  
  where `n` and `m` are the lengths of the two lists.
- **Space:** `O(1)` extra space (we only rearrange existing nodes).

---

## Python Code

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Dummy node to simplify edge cases
        dummy = ListNode()
        tail = dummy

        # Merge while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach any remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next
