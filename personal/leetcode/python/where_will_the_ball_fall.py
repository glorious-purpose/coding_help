"""
1706. Where Will the Ball Fall
Medium
2.5K
146
Companies

You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

    A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
    A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.

We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.



Example 1:

Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

Example 2:

Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.

Example 3:

Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    grid[i][j] is 1 or -1.

"""
from unittest import TestCase, main


class Solution(TestCase):
    def find_ball(self, grid: list[list[int]]) -> list[int]:
        if (width := len(grid[0])) < 2:
            return [-1 for _ in range(width)]
        balls = list(range(width))
        in_play = list(balls)

        def update(stuck, left, right):
            rem = []
            for idx, ball in enumerate(in_play):
                if balls[ball] in stuck:
                    balls[ball] = -1
                    rem.append(idx)
                elif balls[ball] in left:
                    balls[ball] -= 1
                elif balls[ball] in right:
                    balls[ball] += 1
            for i in reversed(rem):
                in_play.pop(i)

        for r_val, row in enumerate(grid):
            stops = []
            r_moves = []
            l_moves = []
            for idx, cell in enumerate(row):
                pos = [balls[x] for x in in_play]
                if idx not in pos:
                    continue
                if cell < 0:
                    # Process left.
                    if idx == 0 or row[idx - 1] > 0:
                        stops.append(idx)
                    else:
                        l_moves.append(idx)

                else:
                    # Process right
                    if idx == width - 1 or row[idx + 1] < 0:
                        stops.append(idx)
                    else:
                        r_moves.append(idx)
            update(stops, l_moves, r_moves)

            if len(in_play) == 0:
                return balls

        return balls

    def setUp(self):
        self.f = self.find_ball

    def test_0(self):
        test = [
            [1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1],
            [1, 1, 1, 1, -1],
            [-1, -1, -1, -1, -1],
        ]
        ans = [1, -1, -1, -1, -1]
        self.assertEqual(self.f(test), ans)

    def test_1(self):
        test = [
            [-1],
        ]
        ans = [-1]
        self.assertEqual(self.f(test), ans)

    def test_2(self):
        test = [
            [1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
            [1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
        ]
        ans = [0, 1, 2, 3, 4, -1]
        self.assertEqual(self.f(test), ans)


if __name__ == "__main__":
    main()