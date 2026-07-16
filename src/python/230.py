from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse in order, stop at k
        counter = 0
        result = None

        def traverse(node):
            nonlocal counter
            nonlocal result

            if result is not None or not node:
                return

            traverse(node.left)

            counter += 1
            if counter == k:
                result = node.val

            traverse(node.right)

        traverse(root)
        return result
