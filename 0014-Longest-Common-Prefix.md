# 0014 - Longest Common Prefix (Easy)

## Problem
Write a function to find the **longest common prefix** string among an array of strings.

If there is **no** common prefix, return an empty string `""`.

---

## Examples

### Example 1
**Input:**  
strs = ["flower","flow","flight"]  
**Output:**  
"fl"

---

### Example 2
**Input:**  
strs = ["dog","racecar","car"]  
**Output:**  
""  
**Explanation:** There is no common prefix among the input strings.

---

## Solution Idea

### Approach — Vertical Scanning
Compare characters column-by-column across all strings:
- Stop as soon as a mismatch is found.
- Build the prefix until mismatch.

This works because a prefix must be shared by all strings at the same character positions.

### Complexity
- **Time:** O(n * m)  
  (n = number of strings, m = prefix length)  
- **Space:** O(1)

---

## Python Code (Final)

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first = strs[0]
        
        for i in range(len(first)):
            for s in strs[1:]:
                if i == len(s) or s[i] != first[i]:
                    return first[:i]
        
        return first
