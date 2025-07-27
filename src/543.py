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

        def calculate_depth(root: Optional[TreeNode], depth: int) -> int:
            if not root:
                return depth

            return 1 + max(
                calculate_depth(root.left, depth), calculate_depth(root.right, depth)
            )

        # base case
        if not root:
            return 0

        # compute the left and right maximum depth
        left_depth = calculate_depth(root.left, 0)
        right_depth = calculate_depth(root.right, 0)
        cur_depth = left_depth + right_depth

        # the diameter is the max of the current depth and whatever diameter we
        # find in the left and right children of the current node
        return max(
            cur_depth,
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
        )
