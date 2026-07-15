from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = list()

        def traverse(root, depth):
            nonlocal queue
            if not root:
                return

            # add to queue at the depth
            if depth < len(queue):
                queue[depth].append(root.val)
            # if depth doesn't exist, add it
            else:
                queue.append([root.val])

            traverse(root.left, depth + 1)
            traverse(root.right, depth + 1)

        traverse(root, 0)
        return queue
