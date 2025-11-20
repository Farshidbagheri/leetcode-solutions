# ------------------------------------------------------------
# Problem: Zigzag Conversion
# LeetCode: https://leetcode.com/problems/zigzag-conversion/
# Difficulty: Medium
# ------------------------------------------------------------
# Approach: Simulate Zigzag Pattern
# - Maintain an array of row-strings with size = numRows.
# - Traverse characters of s while moving a pointer up/down between rows.
# - When pointer hits top or bottom row, reverse direction.
# - Finally, concatenate all rows to produce the zigzag result.
#
# Time Complexity: O(n)
# Space Complexity: O(n) for storing zigzag rows
# ------------------------------------------------------------

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        curr_row = 0
        direction = 1

        for ch in s:
            rows[curr_row] += ch
            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1
            curr_row += direction

        return ''.join(rows)
