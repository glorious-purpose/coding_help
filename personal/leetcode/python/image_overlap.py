"""
835. Image Overlap
Medium
800
257
Companies

You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.



Example 1:

Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1

Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0



Constraints:

    n == img1.length == img1[i].length
    n == img2.length == img2[i].length
    1 <= n <= 30
    img1[i][j] is either 0 or 1.
    img2[i][j] is either 0 or 1.

"""
from unittest import TestCase, main


class Solution(TestCase):
    def largest_overlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        # Get pixel coords from each img
        img_pixels = [[], []]
        dim = len(img1)
        for x in range(dim):
            for y in range(dim):
                if img1[y][x] == 1:
                    img_pixels[0].append((x, y))
                if img2[y][x] == 1:
                    img_pixels[1].append((x, y))
        if len(img_pixels[0]) == 0 or len(img_pixels[1]) == 0:
            return 0
        translations = {}
        for coords in img_pixels[0]:
            for targets in img_pixels[1]:
                translation = (targets[0] - coords[0], targets[1] - coords[1])
                translations[translation] = translations.get(translation, 0) + 1
        return max(translations.values())

    def setUp(self):
        self.func = self.largest_overlap

    def test_0(self):
        self.assertEqual(self.func(img1=[[1, 1, 0], [0, 1, 0], [0, 1, 0]], img2=[[0, 0, 0], [0, 1, 1], [0, 0, 1]]), 3)

    def test_1(self):
        self.assertEqual(self.func(img1=[[1]], img2=[[1]]), 1)

    def test_2(self):
        self.assertEqual(self.func(img1=[[0]], img2=[[0]]), 0)


if __name__ == "__main__":
    main()
