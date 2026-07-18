from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()
        subset = list()

        def backtrack(idx: int):
            # once we've reached beyond the leaf nodes, stop and aggregate
            if idx >= len(nums):
                result.append(subset.copy())
                return

            # the subset tracks if we're including the current number or not
            # there are always two decisions: include or exclude number
            subset.append(nums[idx])
            backtrack(idx + 1)
            # next, don't include the number and run the backtrack
            subset.pop()
            backtrack(idx + 1)

        # start on the first index
        backtrack(0)
        return result
