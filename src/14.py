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

        prefix = ""
        # clever trick to group the all the strings together character by
        # character. no need to make huge for loop and check size of list
        #
        # for example, if strs = ["abc", "defg"],
        # zip(*strs) = [("a","d"), ("b", "e"), ("c", "f")]
        for cs in zip(*strs):
            # if the set has size 1, then all the elements are the same and
            # unique
            if len(set(cs)) == 1:
                # just grab the first character, they're all the same
                prefix += cs[0]
            # stop! we have no more common prefixes since there are different
            # elements in the set
            else:
                break

        return prefix
