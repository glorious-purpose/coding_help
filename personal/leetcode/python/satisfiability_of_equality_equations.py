"""
990. Satisfiability of Equality Equations
Medium

You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.



Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.



Constraints:

    1 <= equations.length <= 500
    equations[i].length == 4
    equations[i][0] is a lowercase letter.
    equations[i][1] is either '=' or '!'.
    equations[i][2] is '='.
    equations[i][3] is a lowercase letter.

"""
from typing import List
import unittest


class Solution(unittest.TestCase):
    def equationsPossible(self, equations: List[str]) -> bool:
        equalities = {}
        letters = set()
        conflicts = False

        # Determine relations
        for entry in equations:
            if entry[0] == entry[3]:
                if entry[1] == "!":
                    return False
                continue
            for ltr in [entry[0], entry[3]]:
                letters.add(ltr)
                if ltr not in equalities:
                    equalities[ltr] = (set(), set())
            if entry[1] == "=":
                equalities[entry[0]][0].add(entry[3])
                equalities[entry[3]][0].add(entry[0])
            else:
                equalities[entry[0]][1].add(entry[3])
                equalities[entry[3]][1].add(entry[0])
        vals = {}
        next_val = 1
        stack = list(letters)
        visited = set()
        # Set Values for letters based on equality
        while len(stack) > 0:
            ltr = stack.pop()
            if ltr in visited:
                continue
            visited.add(ltr)
            ltr_val = vals.get(ltr, None)
            if ltr_val is None:
                for equal_ltr in equalities[ltr][0]:
                    if equal_ltr in vals:
                        ltr_val = vals[equal_ltr]
                        break
                else:
                    ltr_val = next_val
                    next_val += 1
                vals[ltr] = ltr_val
            # Map out equal values first
            for eltr in equalities[ltr][0]:
                if eltr not in visited:
                    stack.append(eltr)
                elv = vals.get(eltr, None)
                if elv is None:
                    vals[eltr] = ltr_val
                elif elv != ltr_val:
                    return False

        # Verify inequalities.
        for ltr in letters:
            ltr_val = vals.get(ltr)
            for iel in equalities[ltr][1]:
                if vals[iel] == ltr_val:
                    return False
        return True

    def solve(self, *args, **kwargs):
        """Interface for easily implementing testing."""
        return self.equationsPossible(*args, **kwargs)

    def test_last_entry(self):
        test = ["c==e", "h==j", "c==c", "k==g", "b!=k", "e==h", "d!=i", "c==a"]
        for _ in range(100000):
            self.assertTrue(self.equationsPossible(test))


if __name__ == "__main__":
    s = Solution()
    test_cases = (
        (["a==b", "b!=a"], False),
        (["b==a", "a==b"], True),
        (["a==b", "b==c", "a==c"], True),
        (["a==b", "b!=c", "c==a"], False),
        (["a!=a"], False),
        (["c==c", "f!=a", "f==b", "b==c"], True),
        (["c==e", "h==j", "c==c", "k==g", "b!=k", "e==h", "d!=i", "c==a"], True),
    )

    for test, answer in test_cases:
        print((result := s.solve(test)), "->", answer, f'{"<- x" if result != answer else ""}', sep="\t")

    # unittest.main()
