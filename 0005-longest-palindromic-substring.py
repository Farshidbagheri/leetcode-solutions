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
            # odd length palindrome
            expand(i, i)
            # even length palindrome
            expand(i, i + 1)

        return s[start:end + 1]
