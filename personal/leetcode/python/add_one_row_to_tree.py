"""
623. Add One Row to Tree
Medium
2.2K
206
Companies

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

    Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
    cur's original left subtree should be the left subtree of the new left subtree root.
    cur's original right subtree should be the right subtree of the new right subtree root.
    If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.



Example 1:

Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Example 2:

Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]



Constraints:

    The number of nodes in the tree is in the range [1, 104].
    The depth of the tree is in the range [1, 104].
    -100 <= Node.val <= 100
    -105 <= val <= 105
    1 <= depth <= the depth of tree + 1

"""
from unittest import TestCase, main
from BST_Tools import TreeNode
from typing import Optional


class Solution(TestCase):
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        stack = [(root, 1)]
        while len(stack) > 0:
            node, cur_dep = stack.pop()
            if cur_dep == depth - 1:
                temp_l = node.left
                temp_r = node.right
                node.left = TreeNode(val, temp_l)
                node.right = TreeNode(val, right=temp_r)
                continue
            if node.right is not None:
                stack.append((node.right, cur_dep + 1))
            if node.left is not None:
                stack.append((node.left, cur_dep + 1))
        return root

    def solve(self, *args, **kwargs):
        return self.addOneRow(*args, **kwargs)

    def test_presets(self):
        null = None
        tests = (
            (([4, 2, 6, 3, 1, 5], 1, 2), [4, 1, 1, 2, null, null, 6, 3, 1, 5]),
            (([4, 2, null, 3, 1], 1, 3), [4, 2, null, 1, 1, 3, null, null, 1]),
        )
        for test, ans in tests:
            res = self.solve(TreeNode.build(test[0]), *test[1:])
            self.assertEqual(res, TreeNode.build(ans))


if __name__ == "__main__":
    main()
