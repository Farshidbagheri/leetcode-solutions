# 0022 - Generate Parentheses (Medium)

## Problem

Given `n` pairs of parentheses, write a function to generate **all combinations** of well-formed parentheses.

Return the answer in **any order**.

---

## Examples

**Example 1**

Input:
```text
n = 3

["((()))","(()())","(())()","()(())","()()()"]


from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []

        def backtrack(cur: str, open_cnt: int, close_cnt: int) -> None:
            if len(cur) == 2 * n:
                res.append(cur)
                return

            if open_cnt < n:
                backtrack(cur + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                backtrack(cur + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return res

n = 1

["()"]
