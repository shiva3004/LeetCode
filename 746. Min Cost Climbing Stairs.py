class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        s1 = cost[0]
        s2 = cost[1]
        for i in range(2, len(cost)):
            s0 = cost[i] + min(s1, s2)
            s1 = s2
            s2 = s0
        return min(s1,s2)
