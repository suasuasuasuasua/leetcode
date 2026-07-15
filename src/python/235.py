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

        # try to find the target
        def search(root, target):
            if not root:
                return False

            if root.val == target.val:
                return True
            elif root.val < target.val:
                return search(root.right, target)
            elif root.val > target.val:
                return search(root.left, target)

        lowest_common = None

        def traverse(root):
            nonlocal lowest_common

            if not root:
                return

            traverse(root.left)
            traverse(root.right)

            # try to search for the two targets as low as possible
            if not lowest_common and search(root, p) and search(root, q):
                lowest_common = root

        traverse(root)
        return lowest_common
