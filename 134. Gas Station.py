class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(cost) == 0:
            return 0
        for i in range(len(gas)):
            if self.canCompleteCircuitHelper(gas[i:] + gas[:i], cost[i:] + cost[:i]):
                return i
        return -1
    
    def canCompleteCircuitHelper(self, gas, cost):
        rem = 0
        for i in range(len(gas)):
            g = rem + gas[i]; c = cost[i]
            if g - c < 0:
                return False
            rem = g - c
        return True
