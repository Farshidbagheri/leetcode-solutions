# 0010 - Regular Expression Matching (Hard)

## Problem
Given strings `s` and pattern `p`, return `true` if `p` matches the entire string `s`.

Pattern rules:
- `.` matches any single character.
- `*` matches zero or more of the previous character.

The match must cover the **entire** string.

---

## Examples

**Example 1**
Input:  
s = "aa", p = "a"  
Output: `false`

**Example 2**  
Input:  
s = "aa", p = "a*"  
Output: `true`

**Example 3**  
Input:  
s = "ab", p = ".*"  
Output: `true`

---

## Solution Idea (Dynamic Programming)

We use DP because:
- Each character depends on previous patterns.
- `*` creates branching states (0, 1, or more repetitions).

Define DP[i][j]:
- True if `s[0:i]` matches `p[0:j]`.

Transitions:
1. If chars match or `.`:
   - `DP[i][j] = DP[i-1][j-1]`
2. If `*` appears at `p[j-1]`:
   - Zero repetition: `DP[i][j] = DP[i][j-2]`
   - One/more: if chars match → `DP[i-1][j]`

Time: O(n*m)  
Space: O(n*m)

---

## Python Code (Final)

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[m][n]
