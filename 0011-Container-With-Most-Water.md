# ------------------------------------------------------------
# Problem: Container With Most Water
# LeetCode: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# ------------------------------------------------------------
# Approach: Two Pointers
# - Use two pointers at the ends of the array.
# - Compute area = min(height[left], height[right]) * (right - left).
# - Move the pointer with the smaller height, since a taller line may increase area.
# - Continue until pointers meet.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            h = min(height[left], height[right])
            best = max(best, h * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best
