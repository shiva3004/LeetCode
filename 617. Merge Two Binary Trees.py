# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        val = 0
        if t1 and t2:
            val = t1.val + t2.val
        elif t1:
            val = t1.val
        elif t2:
            val = t2.val
            
        root = TreeNode(val)
        
        if t1 and t2:
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        elif t1:
            root.left = self.mergeTrees(t1.left, t2)
            root.right = self.mergeTrees(t1.right, t2)
        elif t2:
            root.left = self.mergeTrees(t1, t2.left)
            root.right = self.mergeTrees(t1, t2.right)
            
        return root
