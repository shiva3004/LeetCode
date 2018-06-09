# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(root):
            if root is None:
                return 0
            return max(height(root.left), height(root.right)) + 1
        return height(root)
        
