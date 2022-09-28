"""
838. Push Dominoes
Medium

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

    dominoes[i] = 'L', if the ith domino has been pushed to the left,
    dominoes[i] = 'R', if the ith domino has been pushed to the right, and
    dominoes[i] = '.', if the ith domino has not been pushed.

Return a string representing the final state.



Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:

Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
"""
from unittest import TestCase, main
from typing import List


class Solution(TestCase):
    def pushDominoes(self, dominoes: str) -> str:
        l_ptrs = []
        r_ptrs = []
        dominoes = list(dominoes)
        # Populate pointers
        for idx, char in enumerate(dominoes):
            if char == "L":
                l_ptrs.append(idx)
            elif char == "R":
                r_ptrs.append(idx)
        # Move pointers and affect dominoes
        while len(l_ptrs) > 0 or len(r_ptrs) > 0:
            # Move pointers
            pop_r = []
            pop_l = []
            for idx in range(len(r_ptrs)):
                r_ptrs[idx] += 1
                # Get rid of out of range pointers
                # and pointers that meet another domino.
                if (ptr := r_ptrs[idx]) == len(dominoes) or dominoes[ptr] != ".":
                    pop_r.append(idx)
            for idx in range(len(l_ptrs)):
                l_ptrs[idx] -= 1
                # Get rid of out of range pointers
                # and pointers that meet another domino.
                if (ptr := l_ptrs[idx]) == -1 or dominoes[ptr] != ".":
                    pop_l.append(idx)

            # Remove dead pointers.
            for ptr_idx in sorted(pop_r, reverse=True):
                r_ptrs.pop(ptr_idx)
            for ptr_idx in sorted(pop_l, reverse=True):
                l_ptrs.pop(ptr_idx)

            # Check for dominoes held up by dominoes on both sides
            # Remove from ptr lists
            for ptr in set(r_ptrs).intersection(set(l_ptrs)):
                r_ptrs.pop(r_ptrs.index(ptr))
                l_ptrs.pop(l_ptrs.index(ptr))

            # Affect dominoes
            for ptr in l_ptrs:
                dominoes[ptr] = "L"
            for ptr in r_ptrs:
                dominoes[ptr] = "R"
        return "".join(dominoes)

    def solve(self, *args, **kwargs):
        """Common name used for testing solution."""
        return self.pushDominoes(*args, **kwargs)

    def test_premade_cases(self):
        tests = (("RR.L", "RR.L"), (".L.R...LR..L..", "LL.RR.LLRRLL.."), ("R.", "RR"))
        for test, answer in tests:
            self.assertEqual(self.solve(test), answer)


if __name__ == "__main__":
    main()
