"""
LeetCode 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Approach:
Sliding Window + Hash Map
- Maintain a moving window [left, right] with no duplicate characters.
- Use a hash map to store the last seen index of each character.
- When a duplicate character is found inside the current window,
  move 'left' to one position after the last seen index.
- Update the window size at each step.

Time Complexity: O(n)
Space Complexity: O(min(n, charset))
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}   # char → last index seen
        left = 0        # window start
        best = 0        # longest substring length

        for right, ch in enumerate(s):
            if ch in last_pos and last_pos[ch] >= left:
                left = last_pos[ch] + 1

            last_pos[ch] = right
            best = max(best, right - left + 1)

        return best
