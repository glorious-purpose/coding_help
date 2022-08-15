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
