# https://leetcode.com/problems/contains-duplicate/description/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # problem: given a list of numbers, check if the list contains any
        # duplicates

        # use a set to track whether we've seen an element or not
        seen = set()
        for num in nums:
            # if the number is already in the set, then we've already
            # seen it! there is a duplicate!
            if num in seen:
                return True

            # mark the number as seen
            seen.add(num)

        # if we don't otherwise break early in the loop, then there must not be
        # any duplicates
        return False
