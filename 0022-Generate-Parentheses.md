# 0022 - Generate Parentheses (Medium)

## Problem

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.  
Return the answer in any order.

---

## Examples

**Example 1**

Input:  
`n = 3`  
Output:  
`["((()))","(()())","(())()","()(())","()()()"]`

**Example 2**

Input:  
`n = 1`  
Output:  
`["()"]`

---

## Intuition

A well-formed parentheses string must satisfy:

- The number of opening parentheses `'('` never exceeds `n`.
- At any point, the number of closing parentheses `')'` cannot exceed the number of opening ones.
- The final length must be exactly `2 * n`.

This structure naturally fits a **backtracking** approach:
- Add `'('` when possible.
- Add `')'` only if it keeps the string valid.
- Build step-by-step until the full valid string is formed.

---

## Algorithm

1. Create a result list to store valid combinations.
2. Use recursive backtracking with arguments:
   - `current`: string built so far
   - `open_count`: number of `'('` used
   - `close_count`: number of `')'` used
3. If the length of `current` is `2 * n`, store it.
4. If `open_count < n`, add `'('` and recurse.
5. If `close_count < open_count`, add `')'` and recurse.
6. Return the final list.

---

## Complexity

- **Time Complexity:**  
  The number of valid combinations is the n-th Catalan number: ~`O(4^n / sqrt(n))`.
- **Space Complexity:**  
  Recursive depth: `O(n)`  
  Output size: `O(Cn)` (Catalan number)

---

## Python Code

```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []

        def backtrack(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
