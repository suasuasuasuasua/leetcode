# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        # problem
        # given an integer x, reverse and return the digits in the number
        #
        # quirks
        # - the number x can be positive or negative
        # - ensure that the new number does not under or over flow a certain
        # amount
        # - numbers like 9010000 should be reversed as 109, without the
        # extraneous zeros
        #
        # solution
        # we can parse through the numbers either left to right or right to left
        #
        # it's easier in my brain to parse from the leftmost digit, so this
        # means we have to keep track of the quotient and remainder using
        # various powers of 10
        #
        # we start at some `counter` which is determined by taking the log10 of
        # `x`. we should `floor` this number because it may be fractional
        #
        # using that initial counter, we can count backwards to sus out the
        # leftmost digits

        # zero edge case
        if not x:
            return 0

        # get a copy of the abs value original number
        temp = abs(x)
        # use a counter to iterate through the digits
        initial_counter = counter = math.floor(math.log10(temp))
        # accumulate the numbers
        result = 0

        while temp and counter >= 0:
            q, r = divmod(temp, 10**counter)
            # offset the counter with the inital counter to add the number to
            # the correct decimal place
            # ex: 123
            # 1 -> 1 * 10 ** (2-2) = 1
            # 2 -> 2 * 10 ** (2-1) = 20
            # 3 -> 3 * 10 ** (2-0) = 300
            result += q * (10 ** (initial_counter - counter))
            temp = r
            counter -= 1

        # positive or negative flip
        result *= 1 if x >= 0 else -1

        # sanity check that reversing the number does not cause over/under flow
        if result < -(2**31) or result > (2**31 - 1):
            return 0

        return result
