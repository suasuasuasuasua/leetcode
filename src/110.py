# https://leetcode.com/problems/balanced-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
        # in heights are less than equal to 1
        #
        # we also need to ensure this property for the left and right subtrees
        def check_height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            return 1 + max(check_height(root.left), check_height(root.right))

        if not root:
            return True

        left_height = check_height(root.left)
        right_height = check_height(root.right)

        return (
            abs(left_height - right_height) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )
