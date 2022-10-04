"""41. First Missing Positive
Hard
11.8K
1.5K
Companies

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.



Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1

"""
from unittest import TestCase, main
from random import randint

LEN_MIN = 1
LEN_MAX = 10**5
VAL_MIN = -(2**31)
VAL_MAX = 2**31 - 1

NUM_TESTS = 2000


class Solution(TestCase):
    def firstMissingPositive(self, nums: list[int]) -> int:
        count = 0
        for idx, num in enumerate(nums):
            while 0 < num <= len(nums):
                if idx == num - 1:
                    break
                if nums[num - 1] == num:
                    nums[idx] = 0
                else:
                    temp = nums[num - 1]
                    nums[num - 1] = num
                    nums[idx] = temp
                num = nums[idx]
                count += 1
            else:
                nums[idx] = 0
        if count > len(nums):
            raise TimeoutError(f"Count exceeds length. {count} > {len(nums)}")
        for idx, num in enumerate(nums):
            if num < 1:
                return idx + 1
        return idx + 2

    def solve(self, *args, **kwargs):
        return self.firstMissingPositive(*args, **kwargs)

    def test_presets(self):
        tests = (
            ([1, 2, 0], 3),
            ([3, 4, -1, 1], 2),
            ([7, 8, 9, 11, 12], 1),
            ([7, 8, 9, 11, 12, 1], 2),
            ([1, 2, 3, 4, 6, 7], 5),
            ([1, 1], 2),
            ([10, 4, 16, 54, 17, -7, 21, 15, 25, 31, 61, 1, 6, 12, 21, 46, 16, 56, 54, 12, 23, 20, 38, 63, 2, 27, 35, 11, 13, 47, 13, 11, 61, 39, 0, 14, 42, 8, 16, 54, 50, 12, -10, 43, 11, -1, 24, 38, -10, 13, 60, 0, 44, 11, 50, 33, 48, 20, 31, -4, 2, 54, -6, 51, 6], 3),
        )
        for test, answer in tests:
            res = self.solve(test)
            self.assertEqual(res, answer)

    def test_random(self):
        for _ in range(NUM_TESTS):
            test, answer = self.generate_test()
            res = self.solve(test)
            self.assertEqual(res, answer)

    def generate_test(self):
        test = set()
        this_len = randint(LEN_MIN, LEN_MAX)
        while len(test) < this_len:
            test.add(randint(VAL_MIN, VAL_MAX))
        test = list(test)
        if 1 not in test:
            return test, 1
        s_test = sorted(test)
        for i in range(1, this_len):
            if s_test[i] <= 1:
                continue
            if s_test[i - 1] != s_test[i] - 1:
                return test, s_test[i - 1] + 1


if __name__ == "__main__":
    main()
