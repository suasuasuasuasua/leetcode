# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # problem
        # given the root node of a binary tree, find the depth of the binary
        # tree
        #
        # definition
        # the maximum depth of a binary tree is the number of nodes along the
        # longest path from the root node to the farthest leaf node
        #
        # solution
        # we can use a helper recursive function that tracks the depth as you
        # go down further into the left and right nodes
        # NOTE: we could have just used the function as is without a helper,
        # except that we just return 0 in the `if not root` case
        #
        # the trick is that we start the depth at 0. this ensure that an empty
        # root has a depth of 0.
        # otherwise, we want to check the left and right subtrees. we only take
        # into account the biggest subtree using the `max()` function.
        # finally, we add a 1 to account for the current node, which contributes
        # 1 to the depth
        def check_depth(root: Optional[TreeNode], depth: int) -> int:
            if not root:
                return depth

            left_depth = check_depth(root.left, depth)
            right_depth = check_depth(root.right, depth)

            return 1 + max(left_depth, right_depth)

        return check_depth(root, 0)
