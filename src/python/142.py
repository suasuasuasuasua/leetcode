from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # given a linked list, find where the cycle begins
        # first detect if there is a cycle

        slow = fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break

        # no cycle, don't do anything
        if not has_cycle:
            return None

        # reset the slow pointer back to the head
        # advance slow and fast one by one until they meet
        # this is the starting point
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
