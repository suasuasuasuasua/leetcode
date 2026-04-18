# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @leet start
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # problem
        # given two linked lists where the nodes are stored in reverse order,
        # return the sum as a linked list
        def traverse(l: Optional[ListNode]) -> int:
            head = l

            # track the running sum
            result = 0
            counter = 0
            while head:
                # multiply each number by powers of 10
                result += head.val * (10**counter)
                head = head.next

                # increment the counter
                counter += 1

            return result

        first = traverse(l1)
        second = traverse(l2)
        summation = first + second

        # construct the linked list representation backwards
        q, r = divmod(summation, 10)
        summation = q

        # create the first node
        head = ListNode(r)
        curr = head

        # loop while we can break off (rightmost) numbers from the summation
        while q:
            q, r = divmod(summation, 10)
            summation = q

            # create the new node
            new_node = ListNode(r)
            curr.next = new_node
            curr = new_node

        return head


# @leet end
