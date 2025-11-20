# 0017 - Letter Combinations of a Phone Number (Medium)

## Problem  
Given a string containing digits from **2–9**, return all possible letter combinations that the number could represent.

This follows the mapping of digits to letters on a telephone keypad:

| Digit | Letters |
|-------|---------|
| 2 | abc |
| 3 | def |
| 4 | ghi |
| 5 | jkl |
| 6 | mno |
| 7 | pqrs |
| 8 | tuv |
| 9 | wxyz |

Return the combinations in **any order**.

---

## Examples

### **Example 1**
Input:  
`digits = "23"`  
Output:  
`["ad","ae","af","bd","be","bf","cd","ce","cf"]`

### **Example 2**
Input:  
`digits = "2"`  
Output:  
`["a","b","c"]`

---

## Solution Idea  
This is a **backtracking** problem.

Each digit maps to 3–4 possible characters.  
For each digit, we must try all the letters and build combinations.

### Steps:
1. If input is empty → return empty list.
2. Use a dictionary to map each digit to possible letters.
3. Apply backtracking:
   - Build a path of characters.
   - When the path length equals the number of digits → add to result.
4. Move to the next digit recursively.

### Complexity  
- Let *N* = length of input  
- Each digit has up to 4 options  
- Time complexity: **O(4^N)**  
- Space complexity: **O(N)** for recursion depth

---

## Python Code (With Explanation)

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If no digits, return empty result
        if not digits:
            return []
        
        # Mapping of digits to letters (phone keypad)
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        # Backtracking function
        def backtrack(i, path):
            # If we reached the end of the digits, we found a combination
            if i == len(digits):
                res.append("".join(path))
                return
            
            # Explore each letter mapped to the current digit
            for ch in mapping[digits[i]]:
                path.append(ch)
                backtrack(i + 1, path)
                path.pop()  # backtrack
        
        backtrack(0, [])
        return res
