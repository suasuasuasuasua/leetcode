from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        path = list()

        # track what we've already seen
        def backtrack(used: set):
            if len(used) == len(nums):
                result.append(path.copy())
                return

            # to generate the permutations, we have to check what we've used already
            #
            #      1                  2                   3
            #   2     3           1      3            1       2
            # 3          2     3             1    3              1
            for num in nums:
                if num in used:  # skip numbers that we've already used
                    continue

                used.add(num)  # mark the number as seen
                path.append(num)  # add the number to the path
                backtrack(used)  # continue down with the current number marked
                used.remove(num)  # drop the num
                path.pop()

        backtrack(set())
        return result
