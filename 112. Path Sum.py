# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def hasPathSum(root, sum, val):
            if root is None:
                return False
            if sum == val + root.val and root.left == None and root.right == None:
                return True
            return hasPathSum(root.left, sum, val+root.val) or hasPathSum(root.right, sum, val+root.val)
        
        return hasPathSum(root, sum, 0)
