"""
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.



Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].



Constraints:

    1 <= arr.length <= 1000
    2 <= arr[i] <= 109
    All the values of arr are unique.
"""
from random import randint  # For generating tests.


class Solution:
    def numFactoredBinaryTrees(self, arr: list) -> int:
        count = {n: 1 for n in arr}  # keep track of tree counts for each number
        arr.sort()  # Start with smaller numbers
        MOD = 10**9 + 7

        for i, num in enumerate(arr):
            bp = num // 2
            for j in range(i):
                if arr[j] > bp:
                    break
                if num % (f1 := arr[j]) == 0 and (f2 := num // arr[j]) in arr:
                    count[num] = (count[num] + count[f1] * count[f2]) % MOD

        return sum(count.values()) % MOD

    @staticmethod
    def generate_tests(num_tests=10):

        num_tests = max(min(num_tests, 5000), 1)  # Always generate between 1 and 5000 tests.
        arr_min_length = 1
        arr_max_length = 1000
        min_val = 2
        max_val = 10**9
        for _ in range(num_tests):
            new_test = set()
            test_size = randint(arr_min_length, arr_max_length)
            while len(new_test) < test_size:
                val = randint(min_val, max_val)
                if val in new_test:
                    continue
                new_test.add(val)
            yield sorted(new_test)


if __name__ == "__main__":
    tests = [[2, 4], [2, 4, 5, 10], [18, 3, 6, 2]]
    s = Solution()
    # tests.extend(s.generate_tests(500))
    for test in tests:
        print(s.numFactoredBinaryTrees(test))
