"""
LeetCode 2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

Two non-empty linked lists represent two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
Add the two numbers and return the sum as a linked list.

Approach:
- Walk through both lists simultaneously.
- At each step, sum: current digit of l1 + current digit of l2 + carry.
- The new node's value is (total % 10).
- Update carry = total // 10.
- Continue while there is at least one node left or a non-zero carry.

Time Complexity:  O(max(m, n))
Space Complexity: O(max(m, n)) for the result list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
