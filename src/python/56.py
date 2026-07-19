from collections import deque
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        # start by sorting by start time
        intervals = sorted(intervals, key=lambda i: i[0])

        result = [intervals[0]]
        for interval in intervals:
            prev_start, prev_end = result[-1]
            curr_start, curr_end = interval

            # disjoint intervals
            # prev: [------------]
            # curr:                  [----------------]
            # new:  [------------]   [----------------]
            if prev_end < curr_start:
                result.append(interval)
            # extend the previous interval
            # NOTE: max catches all other cases and extends appropriately
            # prev: [------------]
            # curr: [------------]        equal
            #       [----------------]    curr subsumes
            #        [-----------]        prev subumes
            #        [---------------]    overlap
            else:
                result[-1] = [prev_start, max(prev_end, curr_end)]

        return result
