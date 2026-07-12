import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # there are n piles of bananas
        # the ith pile has piles[i] bananas

        def isValidRate(k: int):
            # does Koko eat all the bananas at this `k` rate?
            # count up the amount of time taken per pile given the rate `k`
            # - we need to .ceil the value because Koko cannot eat more than
            #   one pile per hour
            res = (math.ceil(pile / k) for pile in piles)
            # it must not exceed `h` budget
            return sum(res) <= h

        max_piles = max(piles)
        low = 1
        high = max_piles

        while low < high:
            mid = low + (high - low) // 2

            # if we found a valid rate, try to find an even lower valid rate
            if isValidRate(mid):
                high = mid
            # else, we are probably too small. try a bigger one
            else:
                low = mid + 1

        # NOTE: no need to track `result`
        # this is a classic "find the leftmost value where the predicate flips
        # to True" problem
        # - i.e. find the first smallest viable eating rate
        #
        # these are the invariants
        # - high must always work. < low is not
        # - at the end of the loop, low must equal high
        return low
