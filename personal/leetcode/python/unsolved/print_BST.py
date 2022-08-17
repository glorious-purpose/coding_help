"""
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

    The height of the tree is height and the number of rows m should be equal to height + 1.
    The number of columns n should be equal to 2height+1 - 1.
    Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
    For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
    Continue this process until all the nodes in the tree have been placed.
    Any empty cells should contain the empty string "".

Return the constructed matrix res.



Example 1:

Input: root = [1,2]
Output:
[["","1",""],
 ["2","",""]]

Example 2:

Input: root = [1,2,3,null,4]
Output:
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]



Constraints:

    The number of nodes in the tree is in the range [1, 210].
    -99 <= Node.val <= 99
    The depth of the tree will be in the range [1, 10].
"""

from random import randint
from BST_Tools import TreeNode, BST_generator, Stepper
from typing import Optional, List


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        y_pos = {root.val: 0}  # Location of node in output x,y centered on 0.
        queue = [root]
        height = 0
        # Map out number positions and find height
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is not None:
                next_y = y_pos[node.val] + 1
                y_pos[node.left.val] = next_y
                height = max(height, next_y)
                queue.append(node.left)
            if node.right is not None:
                next_y = y_pos[node.val] + 1
                y_pos[node.right.val] = next_y
                height = max(height, next_y)
                queue.append(node.right)
        output = [["" for _ in range(2 ** (height + 1) - 1)] for _ in range(height + 1)]
        center = len(output[0]) // 2
        x_pos = {root.val: center}
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            output[y_pos[node.val]][x_pos[node.val]] = str(node.val)
            if node.left is not None:
                print(2 ** (height - y_pos[node.val]))
                print(height - y_pos[node.val])
                x_pos[node.left.val] = x_pos[node.val] - 2 ** (height - y_pos[node.val])
                queue.append(node.left)
            if node.right is not None:
                x_pos[node.right.val] = x_pos[node.val] + 2 ** (height - y_pos[node.val])
                queue.append(node.right)
        return output

    @staticmethod
    def generate_tests(num_tests=10):
        num_tests = max(min(num_tests, 1000), 1)
        LEN_MIN = 1
        LEN_MAX = 210  # 210
        VAL_MIN = -99
        VAL_MAX = 99

        for _ in range(num_tests):
            this_test_length = randint(LEN_MIN, LEN_MAX)
            this_test = set()
            while len(this_test) < this_test_length:
                this_test.add(randint(VAL_MIN, VAL_MAX))
            this_test = sorted(this_test)
            test_node = BST_generator(this_test)
            yield test_node


if __name__ == "__main__":
    s = Solution()
    # test_set = s.generate_tests(1)
    # for test in test_set:
    #     result = s.printTree(test)
    #     for row in result:
    #         print(row)
    result = s.printTree(TreeNode(1, left=TreeNode(1)))
    for row in result:
        print(row)
