# https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
from typing import List


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

        def gcd(a: int, b: int) -> int:
            """Euclid's algorithm for greatest common divisors

            See:
                https://en.wikipedia.org/wiki/Euclidean_algorithm

            Args:
                a: the first number
                b: the second number

            Returns:
                the greatest common divisor
            """
            # track the remainder at each step
            while r := a % b:
                a, b = b, r

            return b

        return gcd(smallest, largest)
