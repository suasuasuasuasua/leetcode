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

        # edge cases
        # 1. if x is negative, there is no palindrome possible
        # 2. if x is a multiple of 10, then the code below will break
        #    - the reason why is because x_rev will be 0 while x // 10
        #      continuously pop off the numbers. at the end, we'll claim
        #      that the numbers are palindromes, which is not true
        #    - the number 0 however is a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        x_rev = 0
        while x > x_rev:
            x_rev = (x_rev * 10) + x % 10
            x //= 10

        return x == x_rev or x == x_rev // 10
