from typing import List

class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # intervals are non overlapping
        new_start, new_end = newInterval

        i, n = 0, len(intervals)
        result = list()

        # skip all intervals before the new interval
        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1

        # combine all intervals. the interval that will be inserted may overlap in start
        # grow the left and right sides based on mins and maxes
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        result.append([new_start, new_end])

        # skip all intervals that that after the new interval has ended
        while i < n and intervals[i][0] > new_end:
            result.append(intervals[i])
            i += 1

        return result
