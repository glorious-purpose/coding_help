"""
18. 4Sum
Medium

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]



Constraints:

    1 <= nums.length <= 200
    -109 <= nums[i] <= 109
    -109 <= target <= 109

"""
from unittest import TestCase, main


class Solution(TestCase):
    TESTS = (
        (([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        (([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]]),
        (([-2, -1, -1, 1, 1, 2, 2], 0), [[-2, -1, 1, 2], [-1, -1, 1, 1]]),
    )

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i + 1, n):
                l, r = j + 1, n - 1
                remain = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == remain:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1
                    elif nums[l] + nums[r] > remain:
                        r -= 1
                    else:
                        l += 1
        return list(map(list, ans))

    def adapted_from_combination(self, nums: list[int], target: int) -> list[list[int]]:
        r_nums = []
        count = {}
        for num in nums:
            numc = count.get(num, 0)
            if numc == 4:
                continue
            count[num] = numc + 1
            r_nums.append(num)

        if len(r_nums) == 4 and sum(r_nums) == target:
            return [sorted(r_nums)]
        if len(r_nums) <= 4:
            return []

        answers = set()
        for i in range(len(r_nums) - 3):
            for j in range(i + 1, len(r_nums) - 2):
                for k in range(j + 1, len(r_nums) - 1):
                    for l in range(k + 1, len(r_nums)):
                        iteration = sorted([r_nums[i], r_nums[j], r_nums[k], r_nums[l]])
                        if sum(iteration) == target:
                            answers.add(tuple(iteration))
        return list(map(list, answers))

    def solve(self, *args, **kwargs):
        """Common name for easier testing."""
        return self.fourSum(*args, **kwargs)

    def test_presets(self):
        for test, answer in self.TESTS:
            result = self.solve(*test)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), len(answer), f"\n{result}\n{answer}")
            for unique in answer:
                self.assertIn(unique, result)

    def test_presets_from_combination(self):
        for test, answer in self.TESTS:
            result = self.adapted_from_combination(*test)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), len(answer), f"\n{result}\n{answer}")
            for unique in answer:
                self.assertIn(unique, result)


if __name__ == "__main__":
    # main()
    from timeit import timeit

    num_tests = 10**5
    t = Solution()
    time_taken = timeit("t.test_presets()", globals=globals(), number=num_tests)
    print("Time taken:", time_taken)
    print("Avg. time:", time_taken / num_tests)
    time_taken = timeit("t.test_presets_from_combination()", globals=globals(), number=num_tests)
    print("Time taken:", time_taken)
    print("Avg. time:", time_taken / num_tests)
