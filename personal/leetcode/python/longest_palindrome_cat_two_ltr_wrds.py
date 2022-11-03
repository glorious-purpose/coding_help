"""
2131. Longest Palindrome by Concatenating Two Letter Words
Medium
1.3K
27
Companies

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.



Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".



Constraints:

    1 <= words.length <= 105
    words[i].length == 2
    words[i] consists of lowercase English letters.

"""

from unittest import TestCase, main


class Solution(TestCase):
    def longest_palindrome(self, words: list[str]) -> int:
        pairs = {}
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1
            if pairs.get(word, None) is not None:
                continue
            partner = word[::-1]
            if partner == word or partner in pairs:
                pairs[partner] = word
            else:
                pairs[word] = None
        singles = 0
        couples = 0
        for word, partner in pairs.items():
            if partner is None:
                continue
            if word != partner:
                num_pairs = min(counts[word], counts[partner]) * 2
            else:
                num_pairs = counts[word]
            couples += num_pairs // 2 * 4
            singles = max(singles, num_pairs % 2)
        return couples + singles * 2

    def setUp(self):
        self.func = self.longest_palindrome

    def test_0(self):
        print()
        test, ans = ["lc", "cl", "gg"], 6
        self.assertEqual(self.func(test), ans)
        print()

    def test_1(self):
        print()

        test, ans = ["ab", "ty", "yt", "lc", "cl", "ab"], 8
        self.assertEqual(self.func(test), ans)
        print()

    def test_2(self):
        print()

        test, ans = ["cc", "ll", "xx"], 2
        self.assertEqual(self.func(test), ans)
        print()

    def test_3(self):
        print()

        test, ans = ["dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"], 22
        self.assertEqual(self.func(test), ans)
        print()

    def test_4(self):
        print()

        test, ans = ["ll", "lb", "bb", "bx", "xx", "lx", "xx", "lx", "ll", "xb", "bx", "lb", "bb", "lb", "bl", "bb", "bx", "xl", "lb", "xx"], 26
        self.assertEqual(self.func(test), ans)
        print()


if __name__ == "__main__":
    main()
