"""
39. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []



Constraints:

    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 500

"""
from unittest import TestCase, main
from typing import List


class Solution(TestCase):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pcl = []
        ans = []
        for num in candidates:
            if num < target:
                pcl.append(num)
            elif num == target:
                ans.append([num])
        if len(pcl) == 0:
            return ans
        pcl.sort()
        idxs = {num: idx for idx, num in enumerate(pcl)}

        def iterate_through_pcl(start=pcl[0]):
            for num in pcl[idxs[start] :]:
                yield num
            return

        stack = [iterate_through_pcl()]
        curr_comb = []
        while len(stack) > 0:
            try:
                i = next(stack[-1])
                curr_comb.append(i)
                if sum(curr_comb) < target:
                    stack.append(iterate_through_pcl(curr_comb[-1]))
                    continue
                if sum(curr_comb) == target:
                    ans.append(list(curr_comb))
                curr_comb.pop()
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
            (([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),
            (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
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
