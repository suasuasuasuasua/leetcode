from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # construct the binary tree from two lists of preorder and inorder
        #
        # the pre order list always gives you the subroots of the tree
        # - we can loop over this element by element
        # the in order list is split based on element from the pre order
        # - everything to the left is left child, everything to the right is right child
        def build(preorder, inorder):
            if not preorder or not inorder:
                return

            pnode = preorder.pop(0)
            pivot = inorder.index(pnode)

            node = TreeNode(pnode)
            node.left = build(preorder, inorder[:pivot])
            node.right = build(preorder, inorder[pivot + 1 :])

            return node

        return build(preorder, inorder)
