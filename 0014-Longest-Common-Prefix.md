0014 - Longest Common Prefix (Easy)
Problem

Write a function to find the longest common prefix among an array of strings.

If no common prefix exists → return an empty string "".

Examples
Example 1

Input:
strs = ["flower", "flow", "flight"]
Output: "fl"

Example 2

Input:
strs = ["dog", "racecar", "car"]
Output: ""
Explanation: No common prefix exists.

Solution Idea
Approach — Vertical Scanning (Simple & Clean)

We compare characters column-by-column across all strings:

Pick the first string → treat it as the reference.

For each character position:

Compare that character with the corresponding character in every other string.

If any mismatch occurs → stop.

Everything before the mismatch = longest common prefix.

Why this works?

Because the first mismatch in any column immediately breaks the common prefix.

Complexity

Time: O(N * M)
N = number of strings
M = length of shortest string

Space: O(1)

Python Code (Final)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = ""
        
        # Vertical scanning
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != char:
                    return prefix
            prefix += char
        
        return prefix
