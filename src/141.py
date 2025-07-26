# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # problem
        # given the head of a linked list, determine if there is a cycle in it
        #
        # definition
        # there is a cycle if there is a node in the linked list that can be
        # reached continuously by following the `next` pointer
        #
        # solution
        # the cycle problem can be solved using the slow, fast pointer approach
        # the idea is that the slow pointer will iterate one pointer at a time,
        # while the fast pointer will go two at a time
        #
        # these two pointers are bound to meet if there is a cycle
        # otherwise, the fast will be reach null first

        # begin with the assumption that there is no cycle
        fast = head

        while head and fast:
            # attempt to move the pointers
            # slow moves one `next`
            head = head.next
            try:
                # fast moves by two `next`
                # NOTE: this could throw an exception
                fast = fast.next.next
            except AttributeError:
                return False

            # if these two pointers are ever the same, then there is a cycle
            if head == fast:
                return True

        return False
