class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # inputs:
        #   array of integers
        # outputs:
        #   return all the triplets where i != j != j
        #          and nums[i] + nums[j] + nums[k] == 0

        result = list()
        seen = set()

        # first sort the array
        nums = sorted(nums)

        # second, run the fixed looked up algorithm
        for fixed, fixed_num in enumerate(nums):
            if fixed_num in seen:
                continue
            # a + b + c = 0
            # b + c = -a
            target = -fixed_num

            left = fixed + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    result.append([fixed_num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # the array is sorted -- skip over duplicate numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # the array is sorted -- skip over duplicate numbers
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

            # the inner loop tracks all of the triplets
            # don't even try for numbers that we've already seen
            seen.add(fixed_num)

        return result
