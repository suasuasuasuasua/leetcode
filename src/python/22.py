from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # parens can either be nested or put next to
        # ( x ) or ( ) x
        # (()) or ()()
        result = list()
        path = list()

        def backtrack(nopened, nclosed):
            # there are as many opened and closed
            # for n parens, there must be 2n opened and closed
            if nopened + nclosed == 2 * n:
                result.append("".join(path))
                return

            if nopened < n:
                path.append("(")
                backtrack(nopened + 1, nclosed)
                path.pop()
            if nclosed < nopened:
                path.append(")")
                backtrack(nopened, nclosed + 1)
                path.pop()

        backtrack(0, 0)
        return list(result)
