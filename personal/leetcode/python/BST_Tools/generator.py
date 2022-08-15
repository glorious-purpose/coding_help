from typing import List, Optional
from .treenode import TreeNode


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
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


def sortedArrayToBST_StepByStep(nums: List[int]) -> Optional[TreeNode]:
    start = 0
    end = len(nums) - 1
    center = start + (end - start) // 2
    root = TreeNode(nums[center])
    added = {root.val}
    node = root
    sections = {root.val: (start, center, end)}
    stack = [None, root]
    yield root
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
        yield root
    yield root
