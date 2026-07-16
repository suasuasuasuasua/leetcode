import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # determine if the binary search tree is valid
        #
        # the left subtree contains nodes strictly less than the node's key
        # the right subtree contains nodes strictly greater than the node's key
        # the left and right subtrees must also be binary search tree
        def traverse(node, lower, upper):
            if not node:
                return True

            # fail fast on bad case
            ret = lower < node.val < upper
            if not ret:
                return False

            # pre order traversal
            # tighten the bounds as we descent into the tree
            # - going left, the node beomes the upper bound
            # - going right, the node becomes the lower bound
            return traverse(node.left, lower, node.val) and traverse(
                node.right, node.val, upper
            )

        return traverse(root, -math.inf, math.inf)
