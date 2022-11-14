"""
902. Numbers At Most N Given Digit Set.

Hard
1.2K
94
Companies

Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.



Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation:
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.

Example 3:

Input: digits = ["7"], n = 8
Output: 1



Constraints:

    1 <= digits.length <= 9
    digits[i].length == 1
    digits[i] is a digit from '1' to '9'.
    All the values in digits are unique.
    digits is sorted in non-decreasing order.
    1 <= n <= 109

"""
from unittest import TestCase, main
from time import time


class Solution(TestCase):
    def solve(self, digits: list[str], n: int) -> int:
        count = 0
        dc = len(str(n))
        pos = len(digits)
        for i in range(1, dc):
            count += pos**i

        for i, dig in enumerate(str(n)):
            for char in digits:
                if char < dig:
                    count += pos ** (dc - i - 1)
                else:
                    break
            if dig not in digits:
                break
        return count

    def setUp(self):
        self.start = time()
        print(f"\n---{self._testMethodName}---")

    def tearDown(self):
        print(f"\nEnd - {time() - self.start:.6f}s")

    def test_0(self):
        test = ["1", "3", "5", "7"], 100
        ans = 20
        self.assertEqual(self.solve(*test), ans)

    def test_1(self):
        test = ["1", "4", "9"], 1000000000
        ans = 29523
        self.assertEqual(self.solve(*test), ans)

    def test_2(self):
        test = ["7"], 8
        ans = 1
        self.assertEqual(self.solve(*test), ans)

    def test_3(self):
        test = ["3", "5"], 4
        ans = 1
        self.assertEqual(self.solve(*test), ans)

    def test_4(self):
        test = ["1", "3", "5", "6", "7", "8"], 62774961
        ans = 1222386
        self.assertEqual(self.solve(*test), ans)

    def test_5(self):
        test = ["1", "7"], 200
        ans = 10
        self.assertEqual(self.solve(*test), ans)

    def test_6(self):
        test = ["1", "2", "3", "4", "7", "8", "9"], 32901345
        ans = 2826376
        self.assertEqual(self.solve(*test), ans)

    def test_7(self):
        test = ["3", "4", "8"], 4
        ans = 2
        self.assertEqual(self.solve(*test), ans)


if __name__ == "__main__":
    main()
