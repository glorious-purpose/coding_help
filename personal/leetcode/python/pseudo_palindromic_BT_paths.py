"""
1457. Pseudo-Palindromic Paths in a Binary Tree
Medium

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.



Example 1:

Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:

Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:

Input: root = [9]
Output: 1



Constraints:

    The number of nodes in the tree is in the range [1, 105].
    1 <= Node.val <= 9

"""
from BST_Tools import TreeNode
from typing import Optional
from unittest import main, TestCase


class Solution(TestCase):
    test_trees = (
        (TreeNode(2, TreeNode(1, TreeNode(1), TreeNode(3, right=TreeNode(1))), TreeNode(1)), 1),
        (TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, right=TreeNode(1))), 2),
        (TreeNode(9), 1),
        (TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, right=TreeNode(1))), 2),
    )

    def solve(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        visited = set()
        visited.add(self.tree_hash(root))
        p_paths = 0
        while len(stack) > 0:
            x = stack.pop()
            if x.left is not None:
                n_hash = self.tree_hash(x.left, x)
                if n_hash not in visited:
                    stack.append(x)
                    stack.append(x.left)
                    visited.add(n_hash)
                    continue
            if x.right is not None:
                n_hash = self.tree_hash(x.right, x)
                if n_hash not in visited:
                    stack.append(x)
                    stack.append(x.right)
                    visited.add(n_hash)
                    continue
            if x.left is None and x.right is None:
                nums = {}
                stack.append(x)
                for node in stack:
                    nums[node.val] = nums.get(node.val, 0) + 1
                stack.pop()
                for num in list(nums):
                    if nums[num] % 2 == 0:
                        nums.pop(num)
                if len(nums) in [0, 1]:
                    p_paths += 1
        return p_paths

    def tree_hash(self, node, parent=None):
        p_val = None if parent is None else parent.val
        l_val = None if node.left is None else node.left.val
        r_val = None if node.right is None else node.right.val
        return (p_val, node.val, l_val, r_val)

    def test_0_solve_presets(self):
        for test, answer in self.test_trees:
            print(test, answer, "->", self.solve(test))
            self.assertEqual(self.solve(test), answer)


if __name__ == "__main__":
    main()
