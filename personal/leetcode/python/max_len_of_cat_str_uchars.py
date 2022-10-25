"""
1239. Maximum Length of a Concatenated String with Unique Characters
Medium
2.8K
199
Companies

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.



Constraints:

    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lowercase English letters.

"""
from unittest import TestCase, main
from typing import Optional


class Solution(TestCase):
    def max_length(self, arr: list[str]) -> Optional[int]:
        def get_bitc(word: str) -> int:
            bit_total = 0
            for char in word:
                bit_total |= 1 << ord(char) - ord("a")
            return bit_total.bit_count()

        stack = [enumerate(arr)]
        curr_comb = []
        max_length = 0
        while len(stack) > 0:
            try:
                idx, word = next(stack[-1])
                this_comb = "".join(curr_comb) + word
                if get_bitc(this_comb) < len(this_comb):
                    continue
                max_length = max(max_length, len(this_comb))
                if idx < len(arr) - 1:
                    curr_comb.append(word)
                    stack.append(enumerate(arr[idx + 1 :], idx + 1))
                    continue

            except StopIteration:
                stack.pop()
                if len(curr_comb) > 0:
                    curr_comb.pop()

        return max_length

    def max_length2(self, arr: list[str]) -> int:
        def get_bits(word: str) -> int:
            bit_total = 0
            for char in word:
                bit_total |= 1 << ord(char) - ord("a")
            return bit_total

        # Remove char_sets with duplicates & build bits dict.
        bits = {}
        for idx in range(len(arr) - 1, -1, -1):
            word = arr[idx]
            num = get_bits(word)
            if num.bit_count() < len(word):
                arr.pop(idx)
            else:
                bits[word] = num
        if len(arr) == 0:
            return 0
        arr = sorted(arr, key=lambda a: -len(a))
        stack = [arr[0]]
        visited = set()
        max_length = len(stack[0])

        while len(stack) > 0:
            start = stack.pop()
            max_length = max(max_length, len(start))
            r = bits[start]
            visited.add(start)
            curr_str = start
            for word in arr:
                if word == start:
                    continue
                b = bits[word]
                if r & b == 0:
                    r |= b
                    curr_str += word
                    max_length = max(max_length, len(curr_str))
                elif word not in visited:
                    stack.append(word)
        return max_length

    def test_0(self):
        test, ans = (["un", "iq", "ue"], 4)
        res = self.max_length(test)
        self.assertEqual(res, ans)

    def test_1(self):
        test, ans = (["cha", "r", "act", "ers"], 6)
        res = self.max_length(test)
        self.assertEqual(res, ans)

    def test_2(self):
        test, ans = (["abcdefghijklmnopqrstuvwxyz"], 26)
        res = self.max_length(test)
        self.assertEqual(res, ans)

    def test_3(self):
        test, ans = (["aa", "bb"], 0)
        res = self.max_length(test)
        self.assertEqual(res, ans, test)

    def test_4(self):
        test, ans = (["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"], 16)
        res = self.max_length(test)
        self.assertEqual(res, ans)

    def test_5(self):
        test, ans = (["abc", "ab", "cd", "efg", "ef", "gh"], 8)
        res = self.max_length(test)
        self.assertEqual(res, ans, test)


if __name__ == "__main__":
    main()
