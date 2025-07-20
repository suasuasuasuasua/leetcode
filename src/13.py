# https://leetcode.com/problems/roman-to-integer/description/
class Solution:
    def romanToInt(self, s: str) -> int:
        # the problem is to convert a Roman numeral string to an integer
        # 1. one approach is to use a dictionary mapping to find out the integer
        # value
        #    - we do have six (6) cases to be wary of, in which a preceding
        #      number alters the final number
        roman_mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        for i, c in enumerate(s):
            # retrieve the mapping from the dictionary
            val = roman_mapping[c]

            # add onto the summation
            result += val

            # skip the offset operation for the first number
            if i == 0:
                continue

            # check the previous letter and offset as necessary
            prev_c = s[i - 1]
            # python *magic* to destructure the previous and current character
            # just hard-coded to make solution faster
            # - the better answer is to use prev_c to access the dictionary
            # - i was trying to figure out how to combine all three of these
            #   cases into the same block, but python syntax was throwing me off
            match prev_c, c:
                # I before V (4) and X (9) [-1]
                case ("I", "X" | "V"):
                    offset = 1
                # X before L (40) and C (90) [-10]
                case ("X", "L" | "C"):
                    offset = 10
                # C before D (400) and M (900) [-100]
                case ("C", "D" | "M"):
                    offset = 100
                case _:
                    offset = 0

            # account for the offset
            # note that we multiply by two to account for 1) what we previously
            # added and 2) offset by the correct amount
            result -= offset * 2

        return result
