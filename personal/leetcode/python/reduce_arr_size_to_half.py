"""
1338. Reduce Array Size to The Half
Medium

You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.



Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.



Constraints:

    2 <= arr.length <= 105
    arr.length is even.
    1 <= arr[i] <= 105
"""
from typing import List
from random import randint, choice

LEN_MIN = 2
LEN_MAX = 10**5
VAL_MIN = 1
VAL_MAX = 10**5


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        nums = {}
        for num in arr:
            nums[num] = nums.get(num, 0) + 1
        removed = 0
        rem_count = 0
        length = len(arr)
        for num, count in sorted(nums.items(), key=lambda a: -(a[1])):
            removed += count
            rem_count += 1
            if length - removed <= length // 2:
                break
        return rem_count

    @staticmethod
    def generate_tests(num_tests=10):
        num_tests = max(min(num_tests, 1000), 1)
        for _ in range(num_tests):
            this_length = -1
            while this_length % 2 != 0:
                this_length = randint(LEN_MIN, LEN_MAX)
            this_test = []
            while len(this_test) < this_length:
                num_entries = min(choice((1, 1, 1, 1, 1, 2, 2, 3, 4, randint(5, this_length))), this_length - len(this_test))
                num_val = randint(VAL_MIN, VAL_MAX)
                this_test.extend([num_val for _ in range(num_entries)])
            assert len(this_test) == this_length, f"Length isn't valid: {len(this_test)}:{this_length}"
            yield this_test
