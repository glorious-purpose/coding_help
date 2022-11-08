"""
517. Super Washing Machines
Hard
606
195
Companies

You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any m (1 <= m <= n) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time.

Given an integer array machines representing the number of dresses in each washing machine from left to right on the line, return the minimum number of moves to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.



Example 1:

Input: machines = [1,0,5]
Output: 3
Explanation:
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3
3rd move:    2     1 <-- 3    =>    2     2     2

Example 2:

Input: machines = [0,3,0]
Output: 2
Explanation:
1st move:    0 <-- 3     0    =>    1     2     0
2nd move:    1     2 --> 0    =>    1     1     1

Example 3:

Input: machines = [0,2,0]
Output: -1
Explanation:
It's impossible to make all three washing machines have the same number of dresses.



Constraints:

    n == machines.length
    1 <= n <= 104
    0 <= machines[i] <= 105

"""
from unittest import TestCase, main


class Solution(TestCase):
    def find_min_moves(self, machines: list[int]) -> int:
        if sum(machines) % len(machines) != 0:
            return -1
        target = sum(machines) // len(machines)
        moves = 0
        while True:
            for idx, machine in enumerate(machines):
                if 2 <= machine > target:
                    if idx > 0:
                        machines[idx - 1] += 1
                        machines[idx] -= 1
                        moves += 1
                    if idx < len(machines) - 1:
                        machines[idx + 1] += 1
                        machines[idx] -= 1
                        moves += 1
                    break
            else:
                break
        return moves

    def setUp(self):
        self.func = self.find_min_moves

    def test_0(self):
        test, ans = [1, 0, 5], 3
        self.assertEqual(self.func(list(test)), ans, test)

    def test_1(self):
        test, ans = [0, 3, 0], 2
        self.assertEqual(self.func(list(test)), ans, test)

    def test_2(self):
        test, ans = [0, 2, 0], -1
        self.assertEqual(self.func(list(test)), ans, test)


if __name__ == "__main__":
    main()
