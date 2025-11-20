"""
LeetCode 12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/

Convert an integer in the range [1, 3999] to a Roman numeral.

Approach:
- Use a greedy algorithm with a descending list of (value, symbol) pairs:
  (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
  (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
  (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I").
- For each pair, append its symbol while its value can be subtracted from `num`.
- This naturally handles the subtractive forms (IV, IX, XL, XC, CD, CM).

Time Complexity: O(1)  (the list of pairs is fixed size)
Space Complexity: O(1)
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD",
                   "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]

        res = []
        for v, s in zip(values, symbols):
            while num >= v:
                res.append(s)
                num -= v
        return "".join(res)
