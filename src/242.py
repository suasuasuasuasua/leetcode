# https://leetcode.com/problems/valid-anagram/description/
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the problem is check if `s` and `t` are anagrams of each other
        #
        # solutions
        # 1. sort both of the strings and check if they are equal
        # 2. create two Counter dictionaries to track occurences
        #    verify that the two counters have the same values for each key

        # build the Counter objects
        s_map = defaultdict(int)
        for c in s:
            s_map[c] += 1
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1

        # verify that these have the same keys and values
        return s_map == t_map
