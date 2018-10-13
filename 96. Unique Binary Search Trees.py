class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory = {}
        return self.numTrees1(n, memory)
        
    def numTrees1(self, n,  memory):
        if n <= 1:
            return 1
        left = 0
        right = n-1
        count = 0
        if n in memory:
            return memory[n]
        while right >= 0:
            count += self.numTrees1(left, memory) * self.numTrees1(right, memory)
            left += 1
            right -= 1
        memory[n] = count
        return count
