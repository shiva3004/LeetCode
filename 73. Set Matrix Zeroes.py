class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def make_row_neg(row):
            for i in range(len(matrix[0])):
                if matrix[row][i] != 0:
                    matrix[row][i] = 'a'
                    
        def make_col_neg(col):
            for j in range(len(matrix)):
                if matrix[j][col] != 0:
                    matrix[j][col] = 'a'
                    
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    make_row_neg(i)
                    make_col_neg(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
