class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = self.getHeight(root)
        width = 0
        for i in range(height):
            width = (2 * width) + 1
        matrix = [[ '' for j in range(width)] for i in range(height) ]
        i = 0
        j = width
        index = 0
        self.printTreeHelper(matrix, root, index, i, j)
        return matrix
    
    def printTreeHelper(self, matrix, root, index, i, j):
        if root is None or j < i:
            return
        mid = (i + j) // 2
        matrix[index][mid] = str(root.val)
        self.printTreeHelper(matrix, root.left, index + 1, i, mid - 1)
        self.printTreeHelper(matrix, root.right, index + 1, mid + 1, j)
        
        
        
        
    def getHeight(self, root):
        if root is None:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return max(left, right) + 1
        
