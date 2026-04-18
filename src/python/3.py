# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # problem
        # given a string, find the longest substring that has all unique
        # letters
        #
        # quirks
        # sicne we are interested in substrings, not subsequences
        #
        # solution
        # iterate through all possible substrings, keeping track of some maximum
        # length encountered
        #
        # one approach is a sliding window where we keep track of some "base"
        # we test substrings from the base index to some index i
        # if the current substring is valid, then update the max length
        # accordingly
        # otherwise, we should increment the base index and continue the process
        # to the end

        # start the base and maximum length at 0
        base = max_length = 0

        # iterate through the string and build substrings
        # this will be _at worst_ O(n)
        for i in range(len(s) + 1):
            current = s[base:i]

            # check if the substring has unique values
            curr_length = len(current)
            if len(set(current)) == curr_length:
                # update the max length
                max_length = max(max_length, curr_length)
            # increment the base value to _walk_ across the string
            # this preserves the "sliding window" effect
            #
            # base will lag some amount behind i, which is the max_length seen
            else:
                base += 1

        return max_length
