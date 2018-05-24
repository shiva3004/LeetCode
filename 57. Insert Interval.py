# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        ins_interval = False
        interval_inserted = False
        if len(intervals) == 0:
            return [newInterval]
        elif intervals[-1].end < newInterval.start:
            return intervals + [newInterval]
        elif intervals[0].start > newInterval.end:
            return [newInterval] + intervals
        for i in range(len(intervals)):
            if intervals[i].end < newInterval.start:
                res.append(intervals[i])
                if ins_interval:
                    res.append(newInterval)
                    ins_interval = False
            elif intervals[i].start > newInterval.end:
                if not interval_inserted:
                    res.append(newInterval)
                    interval_inserted = True
                if ins_interval:
                    res.append(newInterval)
                    ins_interval = False
                res.append(intervals[i])
            else:
                s_min = min(intervals[i].start, newInterval.start)
                s_max = max(intervals[i].end, newInterval.end)
                newInterval.start = s_min
                newInterval.end = s_max
                ins_interval = True
                interval_inserted = True
        if ins_interval:
            res.append(newInterval)
        return res
                
