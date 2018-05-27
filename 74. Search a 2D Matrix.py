class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid = (start + end)//2
            if len(matrix[mid]) == 0:
                return False
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return target in matrix[mid]
            elif target < matrix[mid][0]:
                end = mid - 1
            else:
                start = mid + 1
        return False
        
            
