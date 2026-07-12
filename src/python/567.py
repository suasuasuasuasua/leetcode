from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # a permutation of s1, say s1', is s1 with any combination the
        # characters
        # i don't think the problem cares about counting/distincting the
        # permutations, so a counter is fine

        s1_counter = Counter(s1)

        # "slide" a window over s2 to scan for the permutations
        left, right = 0, len(s1)
        s2_substr = s2[left:right]
        s2_counter = Counter(s2_substr)
        while right <= len(s2):
            # consider each substring in s2'
            if s1_counter == s2_counter:
                return True

            # slide left bound, drop the element
            s2_counter[s2[left]] -= 1
            left += 1
            # slide right bound, increment the element
            if right < len(s2):
                s2_counter[s2[right]] += 1
            right += 1

        return False
