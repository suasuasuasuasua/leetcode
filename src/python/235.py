# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # the lowest common ancestor is defined between two nodes p and q as the lowest node in T has both p and q as descendants
        # a node is allowed to be a descandant of itself

        while root:
            # both nodes must be on the left side
            if p.val < root.val and q.val < root.val:
                root = root.left
            # or the right side
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # else, the two must have branched and split off
            # this is the common
            else:
                break

        return root
