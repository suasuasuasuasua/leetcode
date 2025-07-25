# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # problem
        # given the head of two _sorted_ singly linked lists, merge the two
        # lists into one sorted list
        #
        # nuance
        # since both of the lists are known to be sorted, we don't have to
        # handle that
        #
        # solution
        # we can check the front of both lists at the same time.
        # - if x1 is less than x2, then add x1 and advance the linked list
        # - if x1 is greater than x2, then add x2 and advance the linked list
        # - else, we can just add x1 by default

        # Create a new node instead of trying to find the smallest element
        head = curr = ListNode()

        # we should loop while both of the lists are non-empty
        while list1 and list2:
            match list1.val, list2.val:
                case x1, x2 if x1 <= x2:
                    curr.next = list1
                    list1 = list1.next
                case x1, x2 if x1 > x2:
                    curr.next = list2
                    list2 = list2.next
                case _:
                    print("Something has gone horribly wrong!")

            curr = curr.next

        # add the rest of whichever list is remaining
        # the _rest_ should have elements larger than the current list
        # NOTE: really elegant way to set the rest of the list
        #       at the end of the while loop, one of list1 or list2 will be
        #       empty, but not both
        #
        #       moreover, if list1 and list2 are both empty, this won't do
        #       anything
        curr.next = list1 or list2

        # since the head is just an empty ListNode, grab the next one!
        return head.next
