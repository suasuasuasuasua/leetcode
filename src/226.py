# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # problem
        # given the root node of a binary tree, invert the tree and return its
        # root
        #
        # definition
        # inverting a binary tree means swapping the left and right elements of
        # the tree's nodes recursively
        # (see the image on the leetcode description)
        #
        # notes
        # you can traverse a binary tree in three ways
        # 1. pre-order
        #    this results in a root, left, right traversal
        # 2. in-order
        #    this results in a left, root, right traversal
        #    the in-order traversal method returns the nodes in order
        # 3. post-order
        #    this results in a left, right, right traversal
        #
        # solution
        # the pre-order traversal makes the most sense for this inversion.
        # the reason why is that pre-order traversal maintains the structure of
        # the tree.
        # moreover, the inversion is a step that should happen at each parent
        # before we look at the children nodes
        if not root:
            return None

        # swap the left and right nodes immediately
        # NOTE: doesn't matter if the nodes are None, so no need to pattern
        # match
        root.left, root.right = root.right, root.left

        # after inverting the current root's left and right nodes, invert the
        # children nodes
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        # return the base root
        return root
