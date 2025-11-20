# ------------------------------------------------------------
# Problem: String to Integer (atoi)
# LeetCode: https://leetcode.com/problems/string-to-integer-atoi/
# Difficulty: Medium
# ------------------------------------------------------------
# Approach:
# - Skip leading whitespace.
# - Detect optional sign (+ / -).
# - Parse digits until a non-digit appears.
# - Clamp result to 32-bit signed integer range if necessary.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        
        # 2. Check sign
        sign = 1
        if i < n and s[i] in ['+', '-']:
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # 3. Parse digits
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # 4. Check overflow before multiplying
            if result > (2**31 - 1) // 10 or (
                result == (2**31 - 1) // 10 and digit > (7 if sign == 1 else 8)
            ):
                return 2**31 - 1 if sign == 1 else -2**31
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
