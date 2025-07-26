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

        head = None
        if list1 and list2:
            if list1.val <= list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
        elif list1 and not list2:
            head = list1
            list1 = list1.next
        elif not list1 and list2:
            head = list2
            list2 = list2.next

        # we should loop while both of the lists are non-empty
        curr = head
        while list1 and list2:
            match list1.val, list2.val:
                case x1, x2 if x1 <= x2:
                    curr.next = list1
                    list1, curr = list1.next, list1
                case x1, x2 if x1 > x2:
                    curr.next = list2
                    list2, curr = list2.next, list2
                case _:
                    print("Something has gone horribly wrong!")

        # add the rest of whichever list is remaining
        # the _rest_ should have elements larger than the current list
        if curr and list1:
            curr.next = list1
        elif curr and list2:
            curr.next = list2

        return head
