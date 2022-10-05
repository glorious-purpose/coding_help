"""
112. Path Sum
Easy
7K
859
Companies

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.



Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

"""
from unittest import TestCase, main
from BST_Tools import TreeNode
from typing import Optional


class Solution(TestCase):
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stack = [(root, 0)]
        while len(stack) > 0:
            node, tsf = stack.pop()
            tsf += node.val
            if node.left is None and node.right is None:
                if tsf == targetSum:
                    return True
                continue
            if node.right is not None:
                stack.append((node.right, tsf))
            if node.left is not None:
                stack.append((node.left, tsf))
        return False

    def solve(self, *args, **kwargs):
        return self.hasPathSum(*args, **kwargs)

    def test_presets(self):
        null = None
        tests = (
            (([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], 22), True),
            (([1, 2, 3], 5), False),
            (([], 0), False),
        )
        for test, answer in tests:
            res = self.solve(TreeNode.build(test[0]), test[1])
            self.assertEqual(res, answer)


if __name__ == "__main__":
    main()
