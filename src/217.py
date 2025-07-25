# https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # problem: given a list of numbers, check if the list contains any
        # duplicates
        #
        # a few solutions off the top of my head
        # 1. turn the list of numbers into a set
        #    - if the size of the set is not equal to the list of numbers, then
        #      there must have been duplicates
        # 2. use a Counter object to count up the number present
        #    - check if any of the keys have more than one count
        # 3. sort the list and loop over the numbers
        #    - track the previous and current number. if they are the same, then
        #      there must be a duplicate
        #    - time: O(nlogn) because of the sorting

        # convert directly to set and check the length
        return len(set(nums)) != len(nums)
