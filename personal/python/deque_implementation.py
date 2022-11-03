class deq:
    def __init__(self, target: list = None):
        if target is None or len(target) == 0:
            self.left = None
            self.right = None
            self._length = 0
        else:
            self.left, self.right = self.build_queue(target)
            self._length = len(target)

    def build_queue(cls, target: list):
        left_node = None
        cur_node = None
        for val in target:
            if left_node is None:
                left_node = queue_node(val)
                cur_node = left_node
                continue
            new_node = queue_node(val, cur_node)
            cur_node.right = new_node
            cur_node = new_node
        return left_node, cur_node

    def pop_left(self):
        if self.left is None:
            return None
        rnode = self.left
        val = rnode.val
        if rnode.right is not None:
            self.left = rnode.right
            self.left.left = None
        else:
            self.left = None
        self._length -= 1
        del rnode
        return val

    def pop(self, index: int = -1):
        if self.right is None or self.left is None:
            return None
        if index < 0:
            cur_idx = -1
            cur_node = self.right
            while cur_idx > index:
                cur_idx -= 1
                cur_node = cur_node.left
                if cur_node is None:
                    return None
            if cur_node.left is not None:
                cur_node.left.right = cur_node.right
            if cur_node.right is not None:
                cur_node.right.left = cur_node.left
            val = cur_node.val
            self._length -= 1
            del cur_node
            return val

    def __len__(self):
        return self._length

    def __str__(self):
        if self.left is None:
            return str([])
        cur_node = self.left
        contents = [cur_node.val]
        while cur_node.right is not None:
            cur_node = cur_node.right
            contents.append(cur_node.val)
        return str(contents)


class queue_node:
    def __init__(self, val: "queue_node", left: "queue_node" = None, right: "queue_node" = None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = deq(x)
    print(y)
    print(y.pop())
    print(y.pop_left())
    print(y.pop_left())
    print(y)
