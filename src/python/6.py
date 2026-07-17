class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # track row by row
        letters = [list() for _ in range(numRows)]
        counter = 0
        sign = 1
        for c in s:
            letters[counter].append(c)

            counter += 1 * sign
            # flip back and forth on the row bounaries
            if counter == 0 or counter == numRows - 1:
                sign *= -1

        # join the list of lists
        return "".join("".join(r) for r in letters)
