# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # problem
        # given the roots of two binary trees, return True if they are the same
        #
        # definition
        # a binary tree is considered equivalent if they share the exact same
        # structure and the nodes have the same value
        #
        # solution
        # for each node, we should check if the values are equal
        # for each node, the left child for the first tree is equal to the left
        # child of the second tree
        # repeat for the right subtrees
        def dfs(p, q) -> bool:
            match p, q:
                # base case where both are None
                # note: this is trivially true since the structures, if both are None,
                # are actually the same
                case None, None:
                    return True
                # the left node has a value, but the right node is None
                # this means the structure is different
                case TreeNode(), None:
                    return False
                # the left node is None but the right node has a value
                # this means the structure is different
                case None, TreeNode():
                    return False
                # the left and right tree node are present
                case TreeNode(), TreeNode():
                    # check that the node values are the same
                    # also continue checking the left and right nodes recursively
                    return (
                        p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right)
                    )

        return dfs(p, q)
