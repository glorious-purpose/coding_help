"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.



Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.



Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.
"""
from random import randint
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, new_val=0):
        if new_val < self.val:
            if self.left is None:
                self.left = TreeNode(new_val)
            else:
                self.left.add(new_val)
        else:
            if self.right is None:
                self.right = TreeNode(new_val)
            else:
                self.right.add(new_val)

    def __str__(self):
        return f"{self.val} {self.left} {self.right}"

    def __lt__(self, other):
        if isinstance(other, TreeNode):
            return self.val < other.val
        return self.val < other

    def __gt__(self, other):
        if isinstance(other, TreeNode):
            return self.val > other.val
        return self.val > other

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.val == other.val
        return self.val == other

    def __len__(self):
        if self.right is not None:
            right_len = len(self.right)
        if self.left is not None:
            left_len = len(self.left)
        return 1 + right_len + left_len


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums) - 1
        center = start + (end - start) // 2
        root = TreeNode(nums[center])
        added = {root.val}
        node = root
        sections = {root.val: (start, center, end)}
        stack = [None, root]
        while len(added) < len(nums) and node is not None:
            start, center, end = sections[node.val]
            if node.right is None and center < end:
                start = center + 1
                center = start + (end - start) // 2
                new_val = nums[center]
                added.add(new_val)
                node.right = TreeNode(new_val)
                sections[new_val] = (start, center, end)
                stack.append(node)
                node = node.right
            elif node.left is None and start < center:
                end = center - 1
                center = start + (end - start) // 2
                new_val = nums[center]
                added.add(new_val)
                node.left = TreeNode(new_val)
                sections[new_val] = (start, center, end)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
        return root

    @staticmethod
    def generate_tests(num_tests=10):
        num_tests = max(min(num_tests, 1000), 1)
        NUMS_MIN = 1
        NUMS_MAX = 104
        VAL_MIN = -104
        VAL_MAX = 104

        for _ in range(num_tests):
            this_test_length = randint(NUMS_MIN, NUMS_MAX)
            this_test = set()
            while len(this_test) < this_test_length:
                this_test.add(randint(VAL_MIN, VAL_MAX))
            yield sorted(this_test)


if __name__ == "__main__":
    s = Solution()
    test_set = s.generate_tests()
    for test in test_set:
        # print(test)
        print(s.sortedArrayToBST(test))
