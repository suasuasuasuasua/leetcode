class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0

        result = 0
        # track a running set to count characters for the substring
        substr = set()
        while right < len(s):
            # check if the new character is already in the substring
            # if it is, then advance the left bound
            if s[right] in substr:
                substr.remove(s[left])
                left += 1
            # else, grow the right hand side of the sliding window since we
            # haven't seen the character yet
            else:
                substr.add(s[right])
                right += 1

            result = max(result, len(substr))

        return result
