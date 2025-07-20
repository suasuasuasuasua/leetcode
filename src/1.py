# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the problem is that we need to find two indices of numbers in an
        # array such that they add up to the target integer
        #
        # 1. the naiive approach is to hold one number constant and loop over
        # each of the other numbers, checking if the two numbers add up to the
        # target.
        # - the problem with this approach is that the time complexity is O(n^2)
        # 2. an alternative way to think about this problem is to track the
        # differences that makes the current number add up
        # - for example, if the target = 13 and nums[0] = 3, then diff = 10
        # we'll make an entry in the dictionary to point to the index, so
        # mapping[10] = 0
        # - let's say nums[3] = 10, then diff = 3. we can check the
        # dictionary and find that mapping[10] exists already. at this point, we
        # can just return the current index and the saved index
        result = list()
        mapping = dict()
        for i, num in enumerate(nums):
            diff = target - num  # the target should always be greater

            # if we can't find the diff in the mapping, that means we haven't
            # tracked the corresponding number yet
            if not diff in mapping:
                # save the index
                mapping[num] = i
            # if the diff is present in the dictionary, then we have found two
            # numbers that add up to the target
            else:
                result = [i, mapping[diff]]
                break

        return result
