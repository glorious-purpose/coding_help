"""334. Increasing Triplet Subsequence
Medium
5.3K
247
Companies

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.



Constraints:

    1 <= nums.length <= 5 * 105
    -231 <= nums[i] <= 231 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""
from unittest import TestCase, main


class Solution(TestCase):
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        i = 0
        n = len(nums)
        eol = False
        while i < n - 2:
            while nums[i + 1] <= nums[i]:
                i += 1
                if i == n - 2:
                    return False
            j = i + 1
            while nums[j + 1] <= nums[j] and nums[j + 1] > nums[i] or nums[j] < nums[i]:
                j += 1
                if j == n - 1:
                    break
            if j == n - 1:
                i += 1
                continue
            k = j + 1
            while k < n - 1 and nums[k + 1] <= nums[k] and nums[k + 1] > nums[j] or nums[k] < nums[j]:
                k += 1
                if k == n:
                    eol = True
                    break
            if k < n and nums[i] < nums[j] < nums[k]:
                return True
            if j < n - 2:
                i = j
            else:
                i += 1

        return False

    def solve(self, *args, **kwargs):
        return self.increasingTriplet(*args, **kwargs)

    # def test_presets(self):
    #     tests = (
    #         ([1, 2, 3, 4, 5], True),
    #         ([5, 4, 3, 2, 1], False),
    #         ([2, 1, 5, 0, 4, 6], True),
    #         ([1, 5, 4, 2, 3], True),
    #     )
    #
    #     for test, answer in tests:
    #         res = self.solve(test)
    #         self.assertEqual(res, answer, f"'{test}' -> '{answer}' not '{res}'")

    def test_preset_0(self):
        test = [1, 2, 3, 4, 5]
        answer = True
        res = self.solve(test)
        self.assertEqual(res, answer, f"'{test}' -> '{answer}' not '{res}'")

    def test_preset_1(self):
        test = [5, 4, 3, 2, 1]
        answer = False
        res = self.solve(test)
        self.assertEqual(res, answer, f"'{test}' -> '{answer}' not '{res}'")

    def test_preset_2(self):
        test = [2, 1, 5, 0, 4, 6]
        answer = True
        res = self.solve(test)
        self.assertEqual(res, answer, f"'{test}' -> '{answer}' not '{res}'")

    def test_preset_3(self):
        test = [1, 5, 4, 2, 3]
        answer = True
        res = self.solve(test)
        self.assertEqual(res, answer, f"'{test}' -> '{answer}' not '{res}'")

    def test_preset_4(self):
        test = [20, 100, 10, 12, 5, 13]
        answer = True
        res = self.solve(test)
        self.assertEqual(res, answer, f"'{test}' -> '{answer}' not '{res}'")

    def test_preset_5(self):
        test = [1, 2, 2, 1]
        answer = False
        res = self.solve(test)
        self.assertEqual(res, answer, f"'{test}' -> '{answer}' not '{res}'")


if __name__ == "__main__":
    main()
