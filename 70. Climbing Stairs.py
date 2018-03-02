class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory = [0] * (n + 1)
        return self.getClimbStairs(n, memory)
    
    def getClimbStairs(self, n, memory):
        if n <= 1:
            return 1
        if memory[n] == 0:
            memory[n] =  self.getClimbStairs(n-1, memory) + self.getClimbStairs(n-2, memory)
        return memory[n]
        
