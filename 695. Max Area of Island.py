class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_count = 0
        r = len(grid[0])
        c= len(grid)
        for i in range(c):
            for j in range(r):
                if grid[i][j] == 1:
                    count = self.get_area(grid, i, j, r, c)
                    max_count = max(count, max_count)
        return max_count
    
    def get_area(self, grid, i, j, r, c):
        area = 0
        if i < 0 or i >= c or j < 0 or j >= r or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        area += 1
        area += self.get_area(grid, i, j+1, r, c)
        area += self.get_area(grid, i, j-1, r, c)
        area += self.get_area(grid, i+1, j, r, c)
        area += self.get_area(grid, i-1, j, r, c)
        return area
        
