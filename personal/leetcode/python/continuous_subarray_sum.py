"""
523. Continuous Subarray Sum
Medium
3.6K
363
Companies

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.



Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false



Constraints:

    1 <= nums.length <= 105
    0 <= nums[i] <= 109
    0 <= sum(nums[i]) <= 231 - 1
    1 <= k <= 231 - 1

"""
from unittest import TestCase, main


class Solution(TestCase):
    def check_sub_sum(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        if sum(nums) % k == 0:
            return True
        acc_sum = nums[0] % k
        visited = {acc_sum}
        for idx, num in enumerate(nums[1:], 1):
            if num + nums[idx - 1] == 0:
                return True
            acc_sum = (acc_sum + num) % k
            if acc_sum == 0:
                return True
            if acc_sum in visited:
                # Set temp variable that doubles as exit condition
                cur_ac = acc_sum
                acc_sum = num
                # Start looking backwards to see if we've found the subarray.
                for j in range(idx - 1, -1, -1):
                    acc_sum = (acc_sum + nums[j]) % k
                    if acc_sum == 0:
                        return True
                    # If we reach the acc_sum we started with without
                    # finding the subarray, break and continue where
                    # we left off.
                    if acc_sum == cur_ac:
                        break
                acc_sum = cur_ac
            visited.add(acc_sum)
        return False

    def setUp(self):
        self.func = self.check_sub_sum

    def test_0(self):
        test = [23, 2, 4, 6, 7], 6
        ans = True
        self.assertEqual(self.func(*test), ans)

    def test_1(self):
        test = [23, 2, 6, 4, 7], 6
        ans = True
        self.assertEqual(self.func(*test), ans)

    def test_2(self):
        test = [23, 2, 6, 4, 7], 13
        ans = False
        self.assertEqual(self.func(*test), ans)

    def test_3(self):
        test = [0], 1
        ans = False
        self.assertEqual(self.func(*test), ans)

    def test_4(self):
        test = [1, 2, 3], 5
        ans = True
        self.assertEqual(self.func(*test), ans)

    def test_5(self):
        test = [23, 2, 4, 6, 6], 7
        ans = True
        self.assertEqual(self.func(*test), ans)

    def test_6(self):
        with open("test/continuous_subarray_sum_test_6.txt", "r", encoding="utf8") as file:
            test = list(map(int, file.readline().strip().split(","))), 2000000000
        ans = None
        self.assertEqual(self.func(*test), ans)

    def test_7(self):
        test = [1, 0], 2
        ans = False
        self.assertEqual(self.func(*test), ans)


if __name__ == "__main__":
    main()
