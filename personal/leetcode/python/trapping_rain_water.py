"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9



Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
"""
from random import randint
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        # Trim the sides
        while height[-2] >= height[-1]:
            height.pop()
            if len(height) < 3:
                return 0
        height.reverse()
        while height[-2] >= height[-1]:
            height.pop()
            if len(height) < 3:
                return 0
        l_max = height[0]
        ptr = 1
        r_max = max(height[2:])
        captured = 0
        while ptr < len(height) - 1:
            val = height[ptr]
            rain = min(l_max, r_max) - val
            if rain > 0:
                captured += rain
            if val > l_max:
                l_max = val
            if val >= r_max:

                r_max = max(height[ptr + 1 :])
            ptr += 1

        return captured

    @staticmethod
    def generate_tests(num_tests: int = 10) -> List[int]:
        num_tests = min(max(1, num_tests), 1000)
        LEN_MIN = 1
        LEN_MAX = 2 * 10**4
        VAL_MIN = 0
        VAL_MAX = 10**5

        for _ in range(num_tests):
            this_test_length = randint(LEN_MIN, LEN_MAX)
            this_test = [randint(VAL_MIN, VAL_MAX) for _ in range(this_test_length)]
            yield this_test


if __name__ == "__main__":
    s = Solution()
    # print(s.trap([9, 6, 8, 8, 5, 6, 3]))
    tests = s.generate_tests(10)
    for test in tests:
        print(s.trap(test))
