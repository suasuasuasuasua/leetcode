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

        # reverse map the indexes so that it's easy to lookup
        # the preorder val -> inorder index
        mapping = {v: k for k, v in enumerate(inorder)}

        self.counter = 0

        def build(low, high):
            if low > high:
                return

            pnode = preorder[self.counter]
            self.counter += 1
            pivot = mapping[pnode]

            node = TreeNode(pnode)
            node.left = build(low, pivot - 1)
            node.right = build(pivot + 1, high)

            return node

        return build(0, len(inorder) - 1)
