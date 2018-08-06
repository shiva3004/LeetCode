# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        l = self.minDepth(root.left)
        l = l if l !=0 else 236782324
        r = self.minDepth(root.right)
        r = r if r != 0 else 256734872
        return 1+min(l,r)
