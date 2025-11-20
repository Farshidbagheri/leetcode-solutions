# 0016 - 3Sum Closest (Medium)

## Problem

Given an integer array `nums` of length `n` and an integer `target`,  
find three integers in `nums` such that the sum is **closest** to `target`.

Return the **sum** of the three integers.

You may assume that each input would have **exactly one** solution.

---

## Examples

### Example 1
**Input:**  
`nums = [-1, 2, 1, -4]`, `target = 1`  

**Output:**  
`2`  

**Explanation:**  
The sum that is closest to the target is `2` (`-1 + 2 + 1 = 2`).

---

### Example 2
**Input:**  
`nums = [0, 0, 0]`, `target = 1`  

**Output:**  
`0`  

**Explanation:**  
The sum that is closest to the target is `0` (`0 + 0 + 0 = 0`).

---

## Solution Idea (Two Pointers)

We want a triplet whose sum is closest to `target`.

1. **Sort** the array `nums`.
2. Fix an index `i` (this is the first element of the triplet).
3. Use **two pointers** `left` and `right` to choose the other two elements:
   - `left = i + 1`
   - `right = n - 1`
4. For each triple `(i, left, right)`:
   - Compute `s = nums[i] + nums[left] + nums[right]`.
   - If `|s - target|` is smaller than the best difference so far, update `closest`.
   - Move pointers:
     - If `s < target` → increase sum by doing `left += 1`
     - If `s > target` → decrease sum by doing `right -= 1`
     - If `s == target` → this is the best possible answer, return `s`.
5. After checking all positions, return `closest`.

Because the problem guarantees **exactly one solution**, we don't need to worry about ties.

**Time Complexity:** `O(n^2)`  
**Space Complexity:** `O(1)` (ignoring sorting in-place)

---

## Python Code (Final)

```python
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(s - target) < abs(closest - target):
                    closest = s

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return s

        return closest
