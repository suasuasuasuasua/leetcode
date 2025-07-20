# https://leetcode.com/problems/palindrome-number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # the problem is to return whether a number is a boolean or not
        # 1. the naiive (and cheat) solution is to just convert the number to a
        # string (str(x)) and check if the string is equal to its reversed
        return str(x) == str(x)[::-1]
