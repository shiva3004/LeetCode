class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        matrix = [ [ -1 for j in range(len(obstacleGrid[0])) ] for i in range(len(obstacleGrid)) ]
        self.uniquePathsWithObstaclesHelper(matrix, obstacleGrid, 0, 0)
        return matrix[0][0] if matrix[0][0] != -1 else 0
    
    def uniquePathsWithObstaclesHelper(self, matrix, obstacleGrid, i, j):
        if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
            if obstacleGrid[i][j] == 1:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
            return matrix[i][j]
        if i == len(obstacleGrid):
            return 0
        if j == len(obstacleGrid[0]):
            return 0
        if obstacleGrid[i][j] == 1:
            return 0
        if matrix[i][j] != -1:
            return matrix[i][j]
        
        matrix[i][j] = self.uniquePathsWithObstaclesHelper(matrix, obstacleGrid, i + 1, j) + self.uniquePathsWithObstaclesHelper(matrix, obstacleGrid, i, j + 1)
        
        return matrix[i][j]
        
