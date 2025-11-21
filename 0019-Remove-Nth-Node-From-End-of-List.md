# 0019 - Remove Nth Node From End of List (Medium)

## Problem

Given the `head` of a singly linked list, remove the **n-th node from the end** of the list and return its head.

We are guaranteed:
- The list has at least 1 node.
- `1 <= n <= size of the list`.

The follow-up asks: **Can you do this in one pass?**

---

## Examples

**Example 1**  
Input:  
`head = [1,2,3,4,5], n = 2`  
Output:  
`[1,2,3,5]`

**Example 2**  
Input:  
`head = [1], n = 1`  
Output:  
`[]`

**Example 3**  
Input:  
`head = [1,2], n = 1`  
Output:  
`[1]`

---

## Solution Idea (Two Pointers - One Pass)

We want to remove the **n-th node from the end** in a single traversal.

Key trick: use a **dummy node** + **two pointers**:

1. Create a `dummy` node before `head` to handle edge cases (like removing the first node).
2. Set:
   - `left = dummy`
   - `right = head`
3. Move `right` forward `n` steps.
4. Then move both `left` and `right` together until `right` reaches the end.
   - At this point, `left` is exactly **one node before** the node to remove.
5. Skip the target node:  
   `left.next = left.next.next`
6. Return `dummy.next` as the (possibly new) head.

This uses only **one pass** over the list.

---

## Complexity

- **Time:** `O(L)` where `L` is the length of the list  
- **Space:** `O(1)` extra space

---

## Python Code

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Dummy node before head to simplify edge cases
        dummy = ListNode(0, head)

        left = dummy   # slow pointer
        right = head   # fast pointer

        # Move fast pointer n steps ahead
        for _ in range(n):
            right = right.next

        # Move both pointers until fast reaches the end
        while right:
            left = left.next
            right = right.next

        # Now left is just before the node to remove
        left.next = left.next.next

        # Return the new head
        return dummy.next
