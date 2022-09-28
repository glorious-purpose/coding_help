"""
50. Pow(x, n)
Medium

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25



Constraints:

    -100.0 < x < 100.0
    -231 <= n <= 231-1
    -104 <= xn <= 104

"""
from random import randint, uniform
from math import log


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

    @staticmethod
    def generate_tests(num_tests: int = 10) -> tuple:
        num_tests = max(min(num_tests, 1000), 1)
        X_MIN = -100.0
        X_MAX = 100.0
        N_MIN = -(2**31)
        N_MAX = 2**31 - 1
        for _ in range(num_tests):
            x_val = uniform(X_MIN, X_MAX)
            n_val = randint(N_MIN, N_MAX)
            lim = log(10**4, abs(x_val))
            count = 0
            while not -lim <= n_val <= lim:
                n_val = randint(-lim // 1, lim // 1)
            yield x_val, n_val


if __name__ == "__main__":
    s = Solution()
    # print(s.jump([2, 3, 0, 1, 4]))
    tests = s.generate_tests()
    for test in tests:
        print(test, s.myPow(*test), sep=":\n", end="\n\n")
