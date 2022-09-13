"""
45. Jump Game II
Medium

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2



Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 1000

"""
from random import randint
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumper = 0
        jumps = 0
        target = len(nums) - 1
        if jumper == target:
            return 0
        print(nums)
        while True:
            jump_str = nums[jumper]
            if target <= jumper + jump_str:
                print(f"Jumping from rock {jumper}({nums[jumper]}) in to end {target}({nums[target]})")
                return jumps + 1
            h_val = 0
            n_jump = 0
            for rock in range(jumper + 1, jumper + 1 + jump_str):
                val = nums[rock] + rock - jumper
                if val >= h_val:
                    h_val = val
                    n_jump = rock
            print(f"Jumping from rock {jumper}({nums[jumper]}) in to rock {n_jump}({nums[n_jump]})")
            jumper = n_jump
            jumps += 1

    @staticmethod
    def generate_tests(num_tests: int = 10) -> List[int]:
        num_tests = max(min(num_tests, 1000), 1)
        LEN_MIN = 1
        LEN_MAX = 10**4
        VAL_MIN = 0
        VAL_MAX = 1000
        for _ in range(num_tests):
            this_test_length = randint(LEN_MIN, LEN_MAX)
            test = [randint(VAL_MIN, VAL_MAX) for _ in range(this_test_length)]
            if test[0] == 0:
                test[0] = randint(1, VAL_MAX)
            yield test


if __name__ == "__main__":
    s = Solution()
    # print(s.jump([2, 3, 0, 1, 4]))
    tests = s.generate_tests()
    for test in tests:
        print(s.jump(test))
