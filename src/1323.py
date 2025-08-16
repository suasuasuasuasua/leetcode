# https://leetcode.com/problems/maximum-69-number
class Solution:
    def maximum69Number(self, num: int) -> int:
        # problem
        # given a number consistenting of only 6's and 9's, return the
        # largest number possible if we can only "flip" a single digit
        #
        # definition
        # flipping a digit in this context means swapping a 6 with a 9
        # and a 9 with a 6
        #
        # solution
        # track the current number as the greatest possible number seen
        # loop over the rest of the digits by converting the input number
        # to a string
        #
        # if we encounter a 6, try changing it to a 9 and see the
        # resulting maximum number
        # the reason why we don't want to change a 9 to a 6 is because
        # this operation will always decrease the maximum number, rather
        # than increasing it
        max_seen = num

        num_str = str(num)
        for i in range(len(num_str)):
            # break apart the number
            # NOTE: i+1: on the rest slice to start _after_ the current
            # number
            prev, cur, rest = num_str[:i], num_str[i], num_str[i + 1 :]

            # flip the 6 to a 9 to attempt to increase the sum
            if cur == "6":
                cur = "9"

            # reconstruct the number and test the new maximum
            new = int(prev + cur + rest)
            max_seen = max(max_seen, new)

        return max_seen
