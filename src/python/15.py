class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # inputs:
        #   array of integers
        # outputs:
        #   return all the triplets where i != j != j
        #          and nums[i] + nums[j] + nums[k] == 0

        result = set()

        # first sort the array
        nums = sorted(nums)

        # second, run the fixed looked up algorithm
        for fixed, fixed_num in enumerate(nums):
            # a + b + c = 0
            # b + c = -a
            target = -fixed_num

            left = fixed + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    result.add(tuple(sorted([fixed_num, nums[left], nums[right]])))
                    left += 1
                    right -= 1
                    continue
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return [list(r) for r in result]
