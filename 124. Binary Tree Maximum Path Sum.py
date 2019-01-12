# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxPathSumHelper(root)[0]
    
    def maxPathSumHelper(self, root):
        if root is None:
            return (float('-inf'), 0)
        l_val, l_max = self.maxPathSumHelper(root.left)
        r_val, r_max = self.maxPathSumHelper(root.right)
        
                
        return (
            max(l_val, r_val, l_max + r_max + root.val, l_max + root.val, r_max + root.val, root.val), 
            max(l_max + root.val, r_max + root.val, root.val)
        )
    
