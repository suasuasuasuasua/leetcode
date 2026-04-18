# https://neetcode.io/problems/meeting-schedule?list=neetcode150
from typing import List


class Interval(object):
    # Definition of Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # problem
        # given an array of meeting time intervals, determine if a person can add
        # _all_ of the meetings to their schedule without any conflicts
        #
        # solution
        # we need to ensure that these ranges are disjoint of one another

        # start by sorting the intervals by the start time
        intervals = sorted(intervals, key=lambda a: a.start)

        # if the interval list is empty, then we can trivially add _all_ of the
        # meetinsg to the schedule
        if not intervals:
            return True

        # track the previous interval
        prev = intervals[0]
        # loop through the rest of the sorted intervals
        for interval in intervals[1:]:
            # ensure that the previous end is less than the current start
            if prev.end > interval.start:
                return False

            prev = interval

        return True
