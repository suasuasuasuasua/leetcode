# https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # problem: given a list of numbers, check if the list contains any
        # duplicates

        # use a dictionary to track whether we've seen an element or not
        seen = defaultdict(bool)
        for num in nums:
            # if the number is already in the dictionary, then we've already
            # seen it! there is a duplicate!
            if num in seen:
                return True

            # mark the number as seen
            seen[num] = True

        # if we don't otherwise break early in the loop, then there must not be
        # any duplicates
        return False
