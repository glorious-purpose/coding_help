"""
33. Search in Rotated Sorted Array
Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1



Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104

"""
from unittest import TestCase, main
from typing import List


class Solution(TestCase):
    tests = (
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1),
        (([1], 0), -1),
        (([1], 1), 0),
        (([2, 1], 1), 1),
        (([2, 1], 2), 0),
        (([1, 2], 1), 0),
        (([1, 2], 2), 1),
    )

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        l_ptr = 0
        r_ptr = len(nums) - 1

        while not l_ptr > r_ptr:
            m_ptr = l_ptr + (r_ptr - l_ptr) // 2
            if nums[m_ptr] == target:
                return m_ptr
            if nums[l_ptr] <= nums[m_ptr]:
                # l_ptr to m_ptr is sorted
                if nums[l_ptr] <= target < nums[m_ptr]:
                    r_ptr = m_ptr - 1
                else:
                    l_ptr = m_ptr + 1
            else:
                # m_ptr to r_ptr is sorted
                if nums[m_ptr] < target <= nums[r_ptr]:
                    l_ptr = m_ptr + 1
                else:
                    r_ptr = m_ptr - 1
        return -1

    def solve(self, *args, **kwargs):
        return self.search(*args, **kwargs)

    def test_presets(self):
        for test, answer in self.tests:
            results = self.solve(*test)
            self.assertEqual(results, answer, f"{test} -> {answer} != {results}")


if __name__ == "__main__":
    main()
