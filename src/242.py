# https://leetcode.com/problems/valid-anagram/description/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the problem is check if `s` and `t` are anagrams of each other
        #
        # solutions
        # 1. sort both of the strings and check if they are equal

        s = sorted(s)
        t = sorted(t)
        return s == t
