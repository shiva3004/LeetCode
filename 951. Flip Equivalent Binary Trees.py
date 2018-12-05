# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None and root2 is None:
            return True
        elif root1 is None and root2:
            return False
        elif root1 and root2 is None:
            return False
        if root1 and root2:
            if root1.val != root2.val:
                return False
        if self.checkChildren(root1, root2):
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        else:
            return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
    
    def checkChildren(self, root1, root2):
        if root1.left and root2.left and root1.left.val == root2.left.val:
            return True
        elif root1.right and root2.right and root1.right.val == root2.right.val:
            return True
        else:
            return False
