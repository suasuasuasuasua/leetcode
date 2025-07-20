# https://leetcode.com/problems/palindrome-number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # the problem is to return whether a number is a boolean or not
        # 1. the naiive (and cheat) solution is to just convert the number to a
        # string (str(x)) and check if the string is equal to its reversed
        # 2. there is one improvement that could be made to the naiive (1.)
        # solution.
        #    - we don't need to check if the entire string is equal to its
        #      reverse. it would be sufficient to use two pointers (left and
        #      right) iterating from either end that should meet in the middle.
        #      an optimization like this could cut the time in half
        # 3. the final optimization is to avoid converting number to a string at
        # all. this can be done with modulo and division operators to parse out
        # the left and right numbers at each step
        x_rev = 0
        x_copy = x
        while x > 0:
            x_rev = (x_rev * 10) + x % 10
            x //= 10

        return x_copy == x_rev
