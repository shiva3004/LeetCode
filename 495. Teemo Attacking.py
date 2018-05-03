class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        for i in range(len(timeSeries)):
            if i == 0:
                res = duration 
            elif timeSeries[i] - timeSeries[i-1] < duration:
                res += timeSeries[i] - timeSeries[i-1]
            else:
                res += duration
        return res
