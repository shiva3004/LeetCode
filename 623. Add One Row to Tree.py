class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        index = 1
        if d == 1:
            node = TreeNode(v)
            node.left = root
            root = node
        else:
            self.addOneRowHelper(root, v, d, index)
        return root
    
    def addOneRowHelper(self, root, v, d, index):
        if root is None:
            return
        if index < d - 1:
            self.addOneRowHelper(root.left, v, d, index + 1)
            self.addOneRowHelper(root.right, v, d, index + 1)
        elif index == d - 1:
            left = root.left
            right = root.right
            root.left = TreeNode(v)
            root.right = TreeNode(v)
            root.left.left = left
            root.right.right = right
        
