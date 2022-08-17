"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]



Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
"""
from random import randint, choice
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        search_queue = [(0, len(nums))]
        low_index = -1
        high_index = -1

        while len(search_queue) > 0:
            start, end = search_queue.pop(0)
            if start > end:
                continue
            center = start + (end - start) // 2
            if nums[center] == target:
                if low_index == -1 or low_index > center:
                    low_index = center
                if high_index == -1 or high_index < center:
                    high_index = center
            if nums[center] >= target and start <= center - 1:
                search_queue.append((start, center - 1))
            if nums[center] <= target and end >= center + 1:
                search_queue.append((center + 1, end))
        return [low_index, high_index]

    def generate_tests(self, num_tests=10):
        num_tests = max(min(num_tests, 1000), 1)
        LEN_MIN = 0
        LEN_MAX = 10**5
        VAL_MIN = -(10**9)
        VAL_MAX = 10**9
        TARGET_MIN = -(10**9)
        TARGET_MAX = 10**9

        for _ in range(num_tests):
            test = sorted([randint(VAL_MIN, VAL_MAX) for _ in range(randint(LEN_MIN, LEN_MAX))])
            yield test, choice([randint(TARGET_MIN, TARGET_MAX), choice(test)])


if __name__ == "__main__":
    s = Solution()
    test_cases = s.generate_tests()
    for test in test_cases:
        print(s.searchRange(*test), test[1] in test[0], len(test[0]))
