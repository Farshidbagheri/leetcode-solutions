"""
LeetCode Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/

Approach:
- Use a hash map (dictionary) to store numbers we've seen and their indices.
- For each number, check if (target - num) was seen before.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
