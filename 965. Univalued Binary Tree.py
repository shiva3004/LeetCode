# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isUnivalTreeHelper(root, root.val)
    
    def isUnivalTreeHelper(self, root, val):
        if root is None:
            return True
        if root.val != val:
            return False
        return self.isUnivalTreeHelper(root.left, val) and self.isUnivalTreeHelper(root.right, val)
        
