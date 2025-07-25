# https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # the problem is to check if s is a valid palindrome is
        #
        # to start, we should think about what exactly a palindrome is
        # by definition, a palindrome is a string that is the same word reversed
        #
        # solutions
        # 1. the naiive solution is to reverse the entire string and check if it
        #    is equal to `s`

        # NOTE: the problem statement says to sanitize the string by removoing
        # all non-alphanumeric characters AND lowercase
        s = "".join([c for c in s if c.isalnum()])

        # instead of check if the whole string is equal, use two pointers from
        # the left and right
        l, r = 0, len(s) - 1
        while l <= r:
            # grab the character at the current pointer and
            sl = s[l].lower()
            sr = s[r].lower()
            # if the character at the pointers are not equal, then this is not
            # a palindrome
            if sl != sr:
                return False

            # NOTE: always remember to increment and decrement the pointers!
            l += 1
            r -= 1

        return True
