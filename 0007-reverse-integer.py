# ------------------------------------------------------------
# Problem: Reverse Integer
# LeetCode: https://leetcode.com/problems/reverse-integer/
# Difficulty: Medium
# ------------------------------------------------------------
# Approach:
# - Extract digits one by one using modulo and integer division.
# - Rebuild the reversed number.
# - Apply original sign.
# - Return 0 if the reversed value falls outside the 32-bit signed range.
#
# Time Complexity: O(log10(n))
# Space Complexity: O(1)
# ------------------------------------------------------------

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        rev = 0
        
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        
        rev *= sign
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev
