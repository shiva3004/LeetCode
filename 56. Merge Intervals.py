# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        i = 1
        intervals.sort(key=lambda x: x.start)
        while i < len(intervals):
            if intervals[i-1].end >= intervals[i].start and intervals[i-1].end >= intervals[i].end:
                intervals.pop(i)
            elif intervals[i-1].end >= intervals[i].start:
                intervals[i].start = intervals[i-1].start
                intervals.pop(i-1)
            else:
                i += 1
        return intervals
        
