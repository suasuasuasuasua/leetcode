from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal, return last node in the level?
        if not root:
            return list()

        queue = deque([root])
        result = list()
        while queue:
            # track the last number
            last_val = None
            for _ in range(len(queue)):
                node = queue.popleft()
                last_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # the number will have gotten overwritten til this point with the
            # last number since we process left to right
            result.append(last_val)

        return result
