class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # inputs:
        #   array of integers
        # outputs:
        #   return all the triplets where i != j != j
        #          and nums[i] + nums[j] + nums[k] == 0
        results = set()

        # track fixed values that have already been seen/processed
        used_fixed = set()
        # fix an iterator number
        for fixed in range(len(nums)):
            fixed_num = nums[fixed]
            if fixed_num in used_fixed:
                continue
            target = -fixed_num  # a + b + c = 0 -> b + c = -a
            # run two sum algorithm on middle and right
            # the goal is to add up to 0
            seen = dict()
            # start on the index after the fixed
            for running in range(fixed + 1, len(nums)):
                running_num = nums[running]
                if running_num in seen and (
                    fixed != seen[running_num]
                    and fixed != running
                    and seen[running_num] != running
                ):
                    # add a sorted tuple to the set to prevent duplicates
                    results.add(
                        tuple(
                            sorted(
                                (nums[fixed], nums[seen[running_num]], nums[running])
                            )
                        )
                    )
                diff = target - running_num
                seen[diff] = running

            used_fixed.add(fixed_num)

        return list(list(r) for r in results)
