"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.


Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1
"""
from random import randint, choice


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


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Recursive or iterative test?
        x = root
        stack = [None]
        maxs = []
        mins = []
        while True:
            if x.right is not None and x.right.val is not None:
                # Verify right child is larger than self, but smaller than parent.
                vtc = x.right.val
                if (len(maxs) > 0 and vtc > maxs[-1]) or vtc < x.val or (len(mins) > 0 and vtc < mins[-1]):
                    return False
                # We want to revisit this node after exhausting left nodes on this branch.
                stack.append(x)

            # Then check for left node, following left path if possible.
            if x.left is not None and x.left.val is not None:
                # Left branches should not be higher than this node's val
                maxs.append(x.val)

                # Verify left child not smaller than ancestor we have moved right.
                # Verify left child not bigger than self.
                vtc = x.left.val
                if (len(mins) > 0 and vtc < mins[-1]) or (len(maxs) > 0 and vtc >= maxs[-1]):
                    return False

                # Step into left branch.
                x = x.left
                continue

            # If this node doesn't have a left node to step into
            # We need to go to last node on stack to step right.
            x = stack.pop()

            # Make sure we aren't at the end of the stack. Break loop if we are.
            if x is None:
                break

            # Since we are moving right, we don't want future nodes to be below this new node
            mins.append(x.val)

            # We need to scrub the maxs back to next higher ancestor or empty it if we are at root
            while len(maxs) > 0 and maxs[-1] <= x.val:
                maxs.pop()

            # Step into right branch
            x = x.right

        return True

    @staticmethod
    def generate_tests(num_tests=10):
        num_tests = max(min(num_tests, 1000), 1)
        NODES_MIN = 1
        NODES_MAX = 10**4
        VAL_MIN = -(2**31)
        VAL_MAX = 2**31

        for _ in range(num_tests):
            x = [randint(VAL_MIN, VAL_MAX) for _ in range(randint(NODES_MIN, NODES_MAX))]
            root = TreeNode(x[0])
            for i in range(1, len(x)):
                root.add(x[i])
            x = root
            if choice([False for _ in range(4)] + [True for _ in range(6)]):
                while choice([True for _ in range(9)] + [False]):
                    if x.left is None and x.right is None:
                        break
                    options = [x]
                    if x.left is not None:
                        options.append(x.left)
                    if x.right is not None:
                        options.append(x.right)
                    x = choice(options)
                print(x.val, end=" -> ")
                x.val = randint(VAL_MIN, VAL_MAX)
                print(x.val)
            yield root


if __name__ == "__main__":
    s = Solution()
    test_set = s.generate_tests()
    for test in test_set:
        print(s.isValidBST(test))
