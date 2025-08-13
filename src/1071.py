# https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        for i, j in zip(range(1, len(str1) + 1), range(1, len(str2) + 1)):
            if str1[:i] != str2[:j]:
                break
            prefix = str1[:i]
            q1, r1 = divmod(len(str1), len(prefix))
            q2, r2 = divmod(len(str2), len(prefix))

            if q1 * prefix == str1 and q2 * prefix == str2:
                result = prefix

        return result
