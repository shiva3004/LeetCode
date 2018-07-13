class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for j in range(len(grid[0]))] for j in range(len(grid))]
        def minPathSum(grid, i, j, dp):

            if i == len(grid) or j == len(grid[0]):
                return 0
            
            if dp[i][j] != 0:
                return dp[i][j]
            
            if i == len(grid)-1 and j == len(grid[0])-1:
                dp[i][j] = grid[i][j]
                return grid[i][j]
            
            val1 = minPathSum(grid, i, j+1, dp)
            val2 = minPathSum(grid, i+1, j, dp)
            dp[i][j] = max(val1, val2) + grid[i][j] if i == len(grid) -1 or j == len(grid[0])-1 else min(val1, val2) + grid[i][j]
            return dp[i][j]
        return minPathSum(grid, 0, 0, dp)
