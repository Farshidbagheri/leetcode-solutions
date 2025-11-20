"""
LeetCode 9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is a palindrome, and false otherwise.

Approach:
- Negative numbers cannot be palindromes because of the leading '-'.
- Convert the integer to a string and compare it with its reverse.

Time Complexity:  O(k)  where k is the number of digits
Space Complexity: O(k)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
