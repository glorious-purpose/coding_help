"""
40. Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]



Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

"""
from unittest import TestCase, main
from typing import List


class Solution(TestCase):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        visited = set()
        candidates.sort()

        def iterate_through_pcl(start=0):
            for idx in range(start, len(candidates)):
                yield idx
            return

        stack = [iterate_through_pcl()]
        curr_comb = []
        while len(stack) > 0:
            try:
                idx = next(stack[-1])
                num = candidates[idx]
                curr_comb.append(num)
                cct = tuple(curr_comb)
                if cct in visited:
                    curr_comb.pop()
                    continue
                visited.add(cct)
                if sum(curr_comb) < target:
                    stack.append(iterate_through_pcl(idx + 1))
                    continue
                if sum(curr_comb) == target:
                    ans.append(list(curr_comb))
                curr_comb.pop()
                if len(curr_comb) > 0:
                    curr_comb.pop()
                stack.pop()
            except StopIteration:
                if len(curr_comb) > 0:
                    curr_comb.pop()
                stack.pop()
        return ans

    def solve(self, *args, **kwargs):
        return self.combinationSum(*args, **kwargs)

    def test_presets(self):
        tests = (
            (([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
            (([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]),
            (([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27), []),
        )

        for test, answer in tests:
            res = self.solve(*test)
            for ans in res:
                ans.sort()
            res.sort()
            for ans in answer:
                ans.sort()
            answer.sort()
            self.assertEqual(res, answer, f"{test} -> {answer} != {res}")


if __name__ == "__main__":
    main()
