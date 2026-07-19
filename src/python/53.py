from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # given an integer array nums, find the subarray with the largest sum -- return the sum
        # aim for an O(n) solution, so no sorting allowed
        if not nums:
            return 0

        # initially use the first number as the best and current
        best = current = nums[0]
        # iterate through the rest of the numbers
        for num in nums[1:]:
            # decision point: does adding the number increase the current count?
            # if num is better than adding, this essentially "resets" the head of the subarray to this current number
            # else, current + num means we accept the current number into the subarray
            # - note: if current < 0 (below), then current = num
            current = max(num, current + num)
            # track the best number
            best = max(best, current)

        return best
