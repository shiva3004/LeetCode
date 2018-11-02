class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        matrix = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    if not self.canReach(matrix, i, j, set([])):
                        self.changeMatrix(matrix, i, j)
        
        
    def canReach(self, matrix, i, j, visited):
        if (i == len(matrix) - 1 or j == len(matrix[0]) - 1) and matrix[i][j] == 'O':
            return True
        if (i == 0 or j == 0) and matrix[i][j] == 'O':
            return True
        visited.add((i, j))

        neighbours = self.getNeighbours(matrix, i, j)
        #print(i, j, neighbours, visited)
        for neighbour in neighbours:
            a, b = neighbour
            #print(matrix[a][b] == 'O' and ((a, b) not in visited))
            if matrix[a][b] == 'O' and ((a, b) not in visited) and self.canReach(matrix, a, b, visited):
                return True

        return False

    def changeMatrix(self, matrix, i, j):
        neighbours = self.getNeighbours(matrix, i, j)
        matrix[i][j] = 'X'
        for neighbour in neighbours:
            a, b = neighbour
            if matrix[a][b] == 'O':
                self.changeMatrix(matrix, a, b)

    def getNeighbours(self, matrix, i, j):
        s_i = 0 if i == 0 else i - 1
        e_i = i if i == len(matrix) - 1 else i + 1

        s_j = 0 if j == 0 else j - 1
        e_j = j if j == len(matrix[0]) - 1 else j + 1
        res = []
        while s_i <= e_i:
            s_j = 0 if j == 0 else j - 1
            while s_j <= e_j:
                if (s_i == i or s_j == j) and not (s_i == i and s_j == j):
                    res.append((s_i, s_j))
                s_j += 1
            s_i += 1
        return res
            
