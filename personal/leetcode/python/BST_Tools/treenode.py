from typing import Optional


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
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

    @classmethod
    def build(cls, definition: list[int]) -> Optional["TreeNode"]:
        if len(definition) == 0:
            return
        definition = definition[::-1]
        root = TreeNode(definition.pop())
        node_map = [[root]]
        while len(definition) > 0:
            node_map.append([])
            for node in node_map[-2]:
                if node.left is None and (val := definition.pop()) is not None:
                    node.left = TreeNode(val)
                    node_map[-1].append(node.left)
                    if len(definition) == 0:
                        break
                if node.right is None and (val := definition.pop()) is not None:
                    node.right = TreeNode(val)
                    node_map[-1].append(node.right)
                    if len(definition) == 0:
                        break
        return root

    def __str__(self):
        queue = [self]
        output = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None:
                continue
            output.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        return str(output)

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


if __name__ == "__main__":
    test = []
    t = TreeNode.build(test)
    # t.build(test)
    print(t)
