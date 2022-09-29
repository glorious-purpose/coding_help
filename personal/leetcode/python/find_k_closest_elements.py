"""
658. Find K Closest Elements
Medium

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b



Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]



Constraints:

    1 <= k <= arr.length
    1 <= arr.length <= 104
    arr is sorted in ascending order.
    -104 <= arr[i], x <= 104

"""
from unittest import main, TestCase
from typing import List


class Solution(TestCase):
    tests = (
        (([1, 2, 3, 4, 5], 4, 3), [1, 2, 3, 4]),
        (([1, 2, 3, 4, 5], 4, -1), [1, 2, 3, 4]),
        (([1, 1, 1, 10, 10, 10], 1, 9), [10]),
    )

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k:
            return arr
        low = 0
        for i in range(len(arr) - k):
            if len(arr) == k + i or abs(arr[k + i] - x) > abs(arr[i] - x):
                break
            if abs(arr[k + i] - x) < abs(arr[i] - x):
                low = i + 1
        return arr[low : low + k]

    def solve(self, *args, **kwargs):
        return self.findClosestElements(*args, **kwargs)

    def test_presets(self):
        for test, answer in self.tests:
            results = self.solve(*test)
            self.assertEqual(results, answer, f"{test} -> {answer} != {results}")


if __name__ == "__main__":
    main()
