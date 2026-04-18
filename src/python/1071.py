# https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # problem
        # given two strings str1 and str2, return the largest string x such that
        # x divides both str1 and str2
        #
        # definition
        # given two strings s and t, t divides s iff s = t + ... + t
        # (concatenation)
        #
        # solution (naiive)
        # find all possible prefixes for the two strings
        # assert that each prefix can be multiplied k times
        #
        # improved solution
        # if str1 and str2 have a greatest common divisor string, then the
        # following holds:
        #   str1 + str2 = str2 + str1
        #
        # we can then use the gcd algorithm to find the length of the prefix
        # string
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a: int, b: int) -> int:
            """euclid's algorithm"""
            while r := a % b:
                a, b = b, r

            return b

        gcd_index = gcd(len(str1), len(str2))

        return str1[:gcd_index]
