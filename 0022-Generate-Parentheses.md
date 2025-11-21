# 0022 - Generate Parentheses (Medium)

## Problem

Given `n` pairs of parentheses, write a function to generate **all combinations** of well-formed parentheses.

Return the answer in **any order**.

---

## Examples

**Example 1**

Input:
```text
n = 3

["((()))","(()())","(())()","()(())","()()()"]


---

## Intuition

A valid parentheses sequence must follow two rules:

1. The number of opening parentheses `'('` can never exceed `n`.
2. At any point, the number of closing parentheses `')'` must not exceed the number of opening ones.

This makes **Backtracking** the ideal solution:

- We build the string step-by-step.
- At each step, we either:
  - Add `'('` if we still have some remaining.
  - Add `')'` only if we already added more `'('` than `')'`.

This guarantees that every generated string is valid without needing extra validation.

---

## Algorithm

1. Use a helper function `backtrack(current, open_count, close_count)`  
2. If `len(current) == 2 * n`, append it to the result.
3. If `open_count < n`, add `'('` and continue recursion.
4. If `close_count < open_count`, add `')'` and continue recursion.
5. Return the list of all generated combinations.

---

## Complexity

- **Time Complexity:**  
  The number of valid combinations equals the `n`-th Catalan number:  
  **O(4ⁿ / √n)**

- **Space Complexity:**  
  Maximum recursion depth is `O(n)` and output size is `O(Cₙ)`.

---

## Python Code (Final)

```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []

        def backtrack(current: str, open_count: int, close_count: int) -> None:
            # If the current string is complete, store it
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if possible
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' only if it remains valid
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result

["()"]
