from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # build the set of all numbers first (drops duplicates and allows for set member set check)
        seen = set(nums)

        longest = 0
        # step through each number (seen not nums)
        for num in seen:
            # if the number before this number is not in the seen set, then this is the start of a sequence
            if num - 1 not in seen:
                length = 1
                # we're at the head of a sequence, count until we can't anymore
                while num + 1 in seen:
                    num += 1
                    length += 1
                longest = max(longest, length)

        return longest
