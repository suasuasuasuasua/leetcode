from typing import List
import math

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by the ending times
        intervals = sorted(intervals, key=lambda i: i[1])

        last_end = -math.inf
        removed = 0
        for interval in intervals:
            start, end = interval
            # the ends should be ending in order (disjoint)
            if start >= last_end:
                last_end = end
            # if we ever regress, then we can remove it. the interval is essentially redundant
            else:
                removed += 1

        return removed
