from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        # naiive answer -- skip every other house. this doesn't work work because we can
        # jump more than one house
        # ex: [2,1,1,2] == 4
        #
        # odds = sum(num for num in nums[::2])
        # evens = sum(num for num in nums[1::2])
        # return max(odds, evens)

        # constraints: you must skip one or more houses to avoid triggering the security systems
        # there are two choices you must make at each house
        # 1. rob the house
        # 2. skip the house
        #
        # if we decide to rob this house, it must be better than what we counted up to the previous house.
        # the adjacency rule means that if we rob the current house, then we count up 2 houses ago
        #
        # if we don't decide to, then that means whatever we robbed last must have been better
        # best(i) = max(best(i-1), nums[i] + best(i-2))
        best = [0] * len(nums)
        # start with the first two houses
        best[0] = nums[0]  # for houses 0...0, you can only rob the first house
        best[1] = max(
            nums[0], nums[1]
        )  # for houses 0...1, you may rob the first or second house

        for i in range(2, len(nums)):
            best[i] = max(best[i - 1], nums[i] + best[i - 2])

        return max(best)
