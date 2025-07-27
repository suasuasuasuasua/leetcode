# https://leetcode.com/problems/balanced-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # problem
        # given the root of a binary tree, determine if it is height balanced
        #
        # definition
        # a tree is height balanced if the depth of the two subtrees (left and
        # right) never differ by more than one
        # for each node, its left subtree is a balanced tree
        # for each node, its right subtree is a balanced tree
        #
        # solution
        # we should traverse the tree in pre-order and check that the difference
        # in depths are less than equal to 1
        #
        # we also need to ensure this property for the left and right subtrees
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)
            # if the difference in height are ever greater than 1, then that
            # means that the binary trees are not balanced
            if abs(left_height - right_height) > 1:
                self.balanced = False
                return 0

            # compute the depth of the binary tree
            return 1 + max(left_height, right_height)

        if not root:
            return True
        dfs(root)

        # return the final result
        return self.balanced
