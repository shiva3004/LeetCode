class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints = sorted(timePoints)
        minTimeGap = float('inf')
        for i in range(len(timePoints) - 1):
            minTimeGap = min(minTimeGap, self.getTimeDifference(timePoints[i], timePoints[i+1]))
        lastTimePointCalc = self.getTimeDifference(timePoints[-1], "24:00") + self.getTimeDifference("00:00" ,timePoints[0])
        return min(minTimeGap, lastTimePointCalc)
                             
    def getTimeDifference(self, time1, time2):
        return self.getTimeDifferenceHelper(time2) - self.getTimeDifferenceHelper(time1)
    
    def getTimeDifferenceHelper(self, time):
        h, m = time.split(':')
        return int(h) * 60 + int(m)
