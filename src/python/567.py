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
        while right <= len(s2):
            # consider each substring in s2'
            s2_counter = Counter(s2[left:right])

            if s1_counter == s2_counter:
                return True

            left += 1
            right += 1

        return False
