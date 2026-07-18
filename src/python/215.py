from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # input: integer array nums,
        #        integer k
        # output: return kth largest element in the array

        # use heap to track the kth largest
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
