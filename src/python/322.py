from typing import List
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        best = [math.inf] * (amount + 1)
        best[0] = 0

        for a in range(1, amount + 1):  # fill out the best array
            inner_best = math.inf
            for c in coins:  # try each of the coins
                # only consider coins that are smaller than the working amFount
                if c <= a:
                    inner_best = min(inner_best, 1 + best[a - c])
            best[a] = inner_best

        return best[amount] if best[amount] != math.inf else -1
