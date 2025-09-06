# https://leetcode.com/problems/subtree-of-another-tree/
from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # problem
        # given a root tree, check if a subtree is present in the root tree
        #
        # nuance
        # a root tree can be a subroot of itself
        #
        # solution
        # perform a depth first search on the root tree
        # check if the tree is equal at each node (see problem 100.)

        def is_equal(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            match p, q:
                case None, None:
                    return True
                case (TreeNode(), None) | (None, TreeNode()):
                    return False
                case _:
                    return (
                        p.val == q.val
                        and is_equal(p.left, q.left)
                        and is_equal(p.right, q.right)
                    )

        def dfs(p: Optional[TreeNode]) -> bool:
            # base case where we hit an empty node
            # trivially, this root does not contain the subroot
            if not p:
                return False

            # otherwise, check if the current root is equal to the subroot
            # also, we OR the dfs on the left and right children
            return is_equal(p, subRoot) or dfs(p.left) or dfs(p.right)

        return dfs(root)
