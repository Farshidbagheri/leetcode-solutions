# ------------------------------------------------------------
# Problem: Median of Two Sorted Arrays
# LeetCode: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Difficulty: Hard
# ------------------------------------------------------------
# Approach: Binary Search on the Smaller Array
# - Ensure nums1 is the shorter array (A) and nums2 is the longer array (B).
# - Binary search on partition index i in A; compute j in B so that:
#       i + 1 (right side of A) + j + 1 (right side of B) == half of total elements.
# - Use sentinels (-inf, +inf) when the partition touches the ends of arrays.
# - When Aleft <= Bright and Bleft <= Aright, we found the correct partition:
#       * If total length is odd: median = min(Aright, Bright)
#       * If total length is even: median = average of max(Aleft, Bleft) and min(Aright, Bright)
#
# Time Complexity: O(log(min(n, m)))
# Space Complexity: O(1)
# ------------------------------------------------------------

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # Always binary-search on the shorter array
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2          # partition index in A
            j = half - i - 2          # partition index in B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return float(min(Aright, Bright))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            # Move partition in A to the left
            elif Aleft > Bright:
                r = i - 1
            # Move partition in A to the right
            else:
                l = i + 1
