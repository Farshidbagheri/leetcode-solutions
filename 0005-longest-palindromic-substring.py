"""
LeetCode 5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Approach:
Center Expansion
- For each index i, treat i as the center of an odd-length palindrome (i, i),
  and the pair (i, i + 1) as the center of an even-length palindrome.
- Expand pointers l and r outward while s[l] == s[r].
- Track the best (start, end) indices of the longest palindrome seen so far.
- Every palindrome has a center, so checking all centers guarantees coverage.

Time Complexity:  O(n^2) in the worst case
Space Complexity: O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start, end = 0, 0

        def expand(l: int, r: int) -> None:
            nonlocal start, end
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > end - start:
                    start, end = l, r
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd-length palindrome centered at i
            expand(i, i)
            # even-length palindrome centered between i and i+1
            expand(i, i + 1)

        return s[start:end + 1]
