"""
335. Self Crossing
Hard
282
468
Companies

You are given an array of integers distance.

You start at point (0,0) on an X-Y plane and you move distance[0] meters to the north, then distance[1] meters to the west, distance[2] meters to the south, distance[3] meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

Return true if your path crosses itself, and false if it does not.



Example 1:

Input: distance = [2,1,1,2]
Output: true

Example 2:

Input: distance = [1,2,3,4]
Output: false

Example 3:

Input: distance = [1,1,1,1]
Output: true



Constraints:

    1 <= distance.length <= 105
    1 <= distance[i] <= 105

"""
from unittest import TestCase, main


class Solution(TestCase):
    def isSelfCrossing(self, distance: list[int]) -> bool:
        travelled = [0, 0, 0, 0]  # N, W, S, E

        danger = False
        for idx, dis in enumerate(distance):
            curr_idx = idx % 4
            opp_idx = (idx + 2) % 4
            if danger and dis + travelled[curr_idx] >= travelled[opp_idx]:
                return True
            if dis <= travelled[opp_idx]:
                danger = True
            travelled[curr_idx] = dis
        return False

    def test_0(self):
        test, ans = [2, 1, 1, 2], True
        res = self.isSelfCrossing(test)
        self.assertEqual(res, ans)

    def test_1(self):
        test, ans = [1, 2, 3, 4], False
        res = self.isSelfCrossing(test)
        self.assertEqual(res, ans)

    def test_2(self):
        test, ans = [1, 1, 1, 1], True
        res = self.isSelfCrossing(test)
        self.assertEqual(res, ans)

    def test_3(self):
        test, ans = [1, 1, 2, 1, 1], True
        res = self.isSelfCrossing(test)
        self.assertEqual(res, ans)

    def test_4(self):
        test, ans = [3, 3, 4, 2, 2], False
        res = self.isSelfCrossing(test)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    main()
