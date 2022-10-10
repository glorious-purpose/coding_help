"""
1328. Break a Palindrome
Medium
1.1K
533
Companies

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.



Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.



Constraints:

    1 <= palindrome.length <= 1000
    palindrome consists of only lowercase English letters.

"""
from unittest import TestCase, main
from random import randint


class Solution(TestCase):
    def breakPalindrome(self, palindrome: str) -> str:
        aval = ord("a")
        if len(palindrome) < 2:
            return ""

        i = 0
        while i < len(palindrome) // 2:
            cval = ord(palindrome[i])
            if cval > aval:
                return palindrome[:i] + "a" + palindrome[i + 1 :]
            i += 1

        return palindrome[:-1] + chr(ord(palindrome[-1]) + 1)

    def solve(self, *args, **kwargs):
        return self.breakPalindrome(*args, **kwargs)

    def test_presets(self):
        tests = (
            ("abccba", "aaccba"),
            ("a", ""),
            ("aa", "ab"),
        )

        for test, answer in tests:
            res = self.solve(test)
            self.assertEqual(res, answer, f"'{test}' -> '{answer}' not '{res}'")
            self.assertFalse(self.palindrome(res))

    def palindrome(self, test: str) -> bool:
        if len(test) == 0:
            return False
        i = 0
        j = len(test) - 1
        while i < j:
            if test[i] != test[j]:
                return False
            j -= 1
            i += 1
        return True


if __name__ == "__main__":
    main()
