# https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # problem
        # find the greatest common divisor for the two smallest and largest
        # numbers
        #
        # solution
        # 1. find the smallest number
        # 2. find the largest number
        # 3. find the largest common divisor
        if not nums or len(nums) < 2:
            return 1

        # find the smallest and largest numbers in one pass
        smallest = largest = nums[0]
        for num in nums:
            if num < smallest:
                smallest = num
            elif num > largest:
                largest = num

        result = 1
        # loop over numbers starting from the smallest
        # use the inclusive range (+1)
        for i in range(2, smallest+1):
            # update the result iff the smallest and largest numbers are evenly
            # divisble, i.e. the modulo (remainder) is equal to 0
            if smallest % i == 0 and largest % i == 0:
                result = i
            
        return result
