# https://leetcode.com/problems/palindrome-number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # the problem is to return whether a number is a boolean or not
        # 1. the naiive (and cheat) solution is to just convert the number to a
        # string (str(x)) and check if the string is equal to its reversed
        # 2. there is one improvement that could be made to the naiive (1.)
        # solution.
        # - we don't need to check if the entire string is equal to its reverse.
        #   it would be sufficient to use two pointers (left and right)
        #   iterating from either end that should meet in the middle.
        #   an optimization like this could cut the time in half

        x = str(x)
        left, right = 0, len(x) - 1

        while left <= right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1

        return True
