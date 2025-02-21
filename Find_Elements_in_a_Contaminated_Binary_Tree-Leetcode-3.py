# Problem link - https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        self.values = set()
        self.recover_tree(root, 0)  # Start recovery from root with value 0

    def recover_tree(self, node: TreeNode, val: int):
        if not node:
            return
        node.val = val  # Assign correct value
        self.values.add(val)  # Store value in set
        self.recover_tree(node.left, 2 * val + 1)  # Left child formula
        self.recover_tree(node.right, 2 * val + 2)  # Right child formula

    def find(self, target: int) -> bool:
        return target in self.values


# Ignore the input format, just Think that your are given with root of contaminated tree.
