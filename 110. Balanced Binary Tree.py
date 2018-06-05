# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getHeight(root):        
            if root is None:
                return 0
            left = getHeight(root.left)
            if left == -1:
                return -1
            right = getHeight(root.right)
            if right == -1:
                return -1
            if abs(left - right ) > 1:
                return -1
            return max(left, right) + 1
        
        if root is None:
            return True
        return getHeight(root) != -1
        
        
