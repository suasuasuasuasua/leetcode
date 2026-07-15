from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return list()

        queue = deque([root])
        result = list()

        while queue:
            # accumulate the nodes level by level
            # at the top of the loop, the size of the level is the size of the
            # queue
            # - at first iteration, it is 1 (just the root)
            # - at next iteration, the root may add up to 2 children to the
            #   queue
            # - and doubling so on potentially
            level = list()
            n = len(queue)
            for _ in range(n):
                # grab the front of the queue
                node = queue.popleft()
                level.append(node.val)

                # add the left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # append the entire level
            result.append(level)

        return result
