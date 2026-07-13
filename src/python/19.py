from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer approach
        # trailing and leading
        # - both iterate one by one
        # - the leading is n ahead
        # use a dummy node to create a fake node
        result = trailing = ListNode()
        result.next = head
        leading = head

        # advance the leading by `n`
        for i in range(n):
            leading = leading.next

        # advance through the list until the end
        while leading:
            leading = leading.next
            trailing = trailing.next

        # connect the node _before_ the removed node to the one after
        trailing.next = trailing.next.next

        return result.next
