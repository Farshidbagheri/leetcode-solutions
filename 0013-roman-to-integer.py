# 0013 - Roman to Integer (Easy)

## Problem

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Rules:

- Symbols are usually written from largest to smallest from left to right.
- However, in some cases, a smaller value placed before a larger value means subtraction.
- Subtractive cases:
  - I can come before V (5) and X (10) → 4, 9
  - X can come before L (50) and C (100) → 40, 90
  - C can come before D (500) and M (1000) → 400, 900

Given a Roman numeral `s`, convert it to an integer.

---

## Examples

**Example 1**  
Input: `s = "III"`  
Output: `3`

**Example 2**  
Input: `s = "LVIII"`  
Output: `58`  
Explanation: `L = 50`, `V = 5`, `III = 3`.

**Example 3**  
Input: `s = "MCMXCIV"`  
Output: `1994`  
Explanation: `M = 1000`, `CM = 900`, `XC = 90`, `IV = 4`.

---

## Solution Idea

We scan the string from left to right and use a value map for each Roman symbol.

Let `value[c]` be the numeric value of character `c`.

For each position `i`:

- If `value[s[i]] < value[s[i+1]]`, it is a subtractive case, so we **subtract** `value[s[i]]` from the total.
- Otherwise, we **add** `value[s[i]]` to the total.

At the end, `total` is the integer value.

**Complexity**

- Time: `O(n)` — one pass over the string.  
- Space: `O(1)` — fixed-size map of 7 symbols.

---

## Python Code (Final)

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            if i + 1 < n and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total
