"""
38. Count and Say
Medium

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.



Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"



Constraints:

    1 <= n <= 30
"""
# from functools import cache
from unittest import TestCase, main


class Solution(TestCase):
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        n_to_say = self.countAndSay(n - 1)
        this_char = n_to_say[0]
        count = 0
        output = ""
        for char in n_to_say:
            if char == this_char:
                count += 1
            else:
                output += str(count) + this_char
                this_char = char
                count = 1
        output += str(count) + this_char
        return output

    def solve(self, *args, **kwargs):
        return self.countAndSay(*args, **kwargs)

    def test_presets(self):
        tests = (
            (1, "1"),
            (4, "1211"),
        )
        for test, answer in tests:
            res = self.solve(test)
            self.assertEqual(res, answer)


if __name__ == "__main__":
    main()
