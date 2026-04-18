# https://leetcode.com/problems/binary-search/description/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # problem
        # - find a target number from a list of ascending sorted integers
        #
        # constraints
        # - the algorithm must have a time complexity of O(logn)
        #
        # solutions
        # - this is very naturally a binary search problem (hence the problem
        #   title). the O(logn) comes from the fact that we are splitting the
        #   list in half at each step of the binary step algorithm

        lower, upper = 0, len(nums) - 1

        while lower <= upper:
            # recompute the midpoint during each iteration
            midpoint = (upper + lower) // 2
            # use the midpoint to determine the number
            value = nums[midpoint]

            # if the current value is greater than target, then resize the
            # the left side of the "window" to the midpoint
            if value < target:
                lower = midpoint + 1
            # same idea with the right side. we're narrowing down on the left
            # half of the subarray
            elif value > target:
                upper = midpoint - 1
            # else, we've found the element
            else:
                return midpoint

        return -1
