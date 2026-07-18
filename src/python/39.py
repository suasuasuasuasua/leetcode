from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        path = list()

        def backtrack(idx, remaining):
            # if we reach the target exactly, record the path
            if remaining == 0:
                result.append(path.copy())
                return
            # this path failed since we overshot
            elif remaining < 0:
                return
            # in the decision tree, we have the choice to repeatedly include the element
            # we try each and every element
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return result
