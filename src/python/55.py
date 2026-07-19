from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # input: integer array nums
        #        positioned at index=0
        #        each element represents the maximum jump length (j < nums[i]) at that position
        # output: true if we can reach the last index
        reach = 0
        for i in range(len(nums)):
            # if the index == reach point, then there is no more extension possible
            # the reason why is because we've already tried all possible jumps up to `reach`
            if i > reach:
                return False
            # track the maximum possible index that can be reached
            # we try to get better ones by taking which index we're currently on + the jump on the indx
            reach = max(reach, i + nums[i])
            # if the reach extends to the length of the numbers (the last index), then we've found a path
            if reach >= len(nums):
                return True

        return True
