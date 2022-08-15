from .treenode import TreeNode


def isValidBST(root: TreeNode) -> bool:
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
