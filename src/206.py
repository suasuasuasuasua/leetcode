# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # problem
        # given the head of a singly linked list, reverse the linked list
        #
        # example
        # 0 (p)   (c)
        #  None    1 -> 2 -> 3 -> None
        # 1 (p)   (c)  (n)
        #  None <- 1    2 -> 3 -> None
        # 2       (p)  (c)  (n)
        #  None <- 1 <- 2    3 -> None
        # 3            (p)  (c)   (n)
        #  None <- 1 <- 2 <- 3    None
        # solution
        # use three pointers
        # 1. the first pointer tracks the previous node
        # 2. the second pointer tracks the current node
        # 3. the third pointer tracks the next node
        #    this one is used so we don't lose track of the rest of the list

        # start at the head
        prev = next = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            # swap the current, previous, and next nodes
            curr, prev = next, curr

        # NOTE: we return the prev node because curr will be None by the end of
        # the while loop
        #
        # we could otherwise include an if-else statement
        return prev
