class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R = len(M)
        C = len(M[0])
        res = [[0] * C for _ in M]
        for i in range(0, R):
            for j in range(0, C):
                res[i][j] = self.get_average_grey_scale(M, i, j)
        return res
    
    def get_average_grey_scale(self, M, i, j):
        R = len(M)
        C = len(M[0])
        count = val = 0
        for r in range(i-1, i+2):
            for c in range(j-1, j+2):
                if r >= 0 and r < R and c >= 0 and c < C:
                    val += M[r][c]
                    count += 1
        return val/count
