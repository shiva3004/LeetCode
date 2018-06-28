class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [[None for i in range(n)] for j in range(m)]
        def uniquePaths(i, j, m, n):
            if i > m:
                return 0
            if j > n:
                return 0
            if (i == m and j == n) or matrix[i][j] is not None:
                if matrix[i][j] is None:
                    matrix[i][j] = 1
                return matrix[i][j]
            count = uniquePaths(i, j+1, m, n)
            count += uniquePaths(i+1, j, m, n)
            matrix[i][j] = count
            return count
        return uniquePaths(0, 0, m-1, n-1)
