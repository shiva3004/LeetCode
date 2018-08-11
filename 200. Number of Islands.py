class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def getAdjacent(grid, index):
            [i, j] = index
            res = []
            r = len(grid)
            c = len(grid[0])
            x = max(i-1, 0)
            while x < min(i+2, r):
                if x != i:
                    res.append([x, j])
                x += 1
            y = max(j-1, 0)
            
            while y < min(j+2, c):
                if y != j:
                    res.append([i, y])
                y += 1
            return res
            
        def bfsIslands(grid, index):
            [i, j] = index
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            adj = getAdjacent(grid, [i,j])
            for l in adj:
                bfsIslands(grid, l)
        #print(getAdjacent(grid, [3, 1]))   
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "0":
                    count += 1
                    bfsIslands(grid, [i, j])
        return count
    
