class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, numRows+1):
            t = []
            for j in range(i):
                if j == 0 or j == i-1:
                    t.append(1)
                else:
                    t.append(res[i-2][j-1] + res[i-2][j])
            res.append(t)
        return res
                    
