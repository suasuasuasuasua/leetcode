# https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # the problem is about returning the longest common prefix from a list
        # of strings.
        #
        # immediately, that screams a trie probem. this is a tree that is
        # specifically for storing prefixes for words, making the lookup easier
        # - note that this tree does not have to be binary
        #
        # another solution could be to just iterate through all of the strings
        # simultaneously. for example, if i=0, then check if all strings at i=0
        # are the same value until they aren't
        # - i imagine that this is the _very_ naiive solution but it may be
        #   worth doing to see what can be improved

        # sanity check if
        # 1. the list is empty
        # 2. any of the strings in the list are empty
        if not strs or any(len(s) == 0 for s in strs):
            return ""

        # we should only check up to the smallest string in the list
        min_n = min(len(s) for s in strs)
        result = ""
        # loop over 0 -> min_n
        for i in range(min_n):
            # grab the current characters from all of the strings at the same
            # time using i
            current_chars = set(s[i] for s in strs)

            # ensure that the length is 1, meaning that all the elements at
            # index i are the same, meaning that they share a prefix still
            if len(current_chars) == 1:
                # add it to the result string
                result += list(current_chars)[0]
            else:
                break

        return result
