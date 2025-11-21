# 0020 - Valid Parentheses (Easy)

## Problem
Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

A string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket.

---

## Examples

**Example 1**  
Input: `s = "()"`  
Output: `true`

**Example 2**  
Input: `s = "()[]{}"`  
Output: `true`

**Example 3**  
Input: `s = "(]"`  
Output: `false`

**Example 4**  
Input: `s = "([)]"`  
Output: `false`

**Example 5**  
Input: `s = "{[]}"`  
Output: `true`

---

## Solution (Using Stack)

We use a stack to track opening brackets.

### Idea:
- Every opening bracket is pushed onto the stack.
- Every closing bracket must match the **latest opening bracket**.
- If mismatch → invalid.
- If stack is empty at the end → valid.

### Time Complexity:
- **O(n)** – one pass through the string.

### Space Complexity:
- **O(n)** – stack can grow to the size of input.

---

## Python Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_map = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in close_map.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != close_map[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
```
