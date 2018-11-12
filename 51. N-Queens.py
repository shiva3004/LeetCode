class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def solveNQueensHelper(matrix, index):
            #print(matrix, index)
            if index == -1:
                strs = getStrsFromMatrix(matrix)
                res.append(strs)
                return False
            
            for i in range(len(matrix) - 1, -1, -1):
                #print(matrix, index, i)
                if validQueenPosition(matrix, index, i):
                    #print(matrix, index, i, True)
                    matrix[index][i] = 'Q'
                    if solveNQueensHelper(matrix, index - 1):
                        pass
                    else:
                        matrix[index][i] = '.'
            return False
        
        def validQueenPosition(matrix, row, col):
            s_i = 0; e_i = len(matrix) - 1
            s_j = 0; e_j = len(matrix) - 1
            #print(row, col, 1)
            for j in range(len(matrix)):
                if matrix[row][j] == 'Q':
                    return False
            
            for i in range(len(matrix)):
                #print(i, col)
                if matrix[i][col] == 'Q':
                    return False
                
            i = row; j = col
            while i >= 0 and j >= 0:
                if matrix[i][j] == 'Q':
                    return False
                i -= 1; j -= 1
                
            i = row; j = col
            while i <= e_i and j <= e_j:
                if matrix[i][j] == 'Q':
                    return False
                i += 1; j += 1
            
            i = row; j = col
            while i >= 0 and j <= e_j:
                if matrix[i][j] == 'Q':
                    return False
                i -= 1; j += 1
            
            i = row; j = col
            while i <= e_i and j >= 0:
                if matrix[i][j] == 'Q':
                    return False
                i += 1; j -= 1
            
            return True
                
        def getStrsFromMatrix(matrix):
            res = []
            for row in matrix:
                res.append(''.join(row))
            return res
        
        matrix = [[ '.' for j in range(n)] for i in range(n)]
        res = []
        index = n - 1
        solveNQueensHelper(matrix, index)
        return res
        
        
