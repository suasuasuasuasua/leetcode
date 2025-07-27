# https://leetcode.com/problems/diameter-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # problem
        # given the root of a binary tree, calculate the diameter of the binary
        # tree
        #
        # definition
        # the diameter of a binary tree is the length of the longest
        # between any two nodes in the tree. that path may or may not cross
        # through the root
        # the length of a path between two tree nodes is the number of edges
        # between them
        #
        # solution
        # the longest path is going to be from one side of the tree to the other
        # we can calculate this by tracking the maximum depth on the left plus
        # the maximum depth on the right

        # global var that tracks the maximum diameter
        diameter = 0

        def calculate_depth(root: Optional[TreeNode], depth: int) -> int:
            if not root:
                return depth

            # the diameter is the max of the current depth and whatever diameter we
            # find in the left and right children of the current node
            left_height = calculate_depth(root.left, depth)
            right_height = calculate_depth(root.right, depth)
            nonlocal diameter
            diameter = max(diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        # base case
        if not root:
            return 0

        # run the
        calculate_depth(root, 0)

        return diameter
