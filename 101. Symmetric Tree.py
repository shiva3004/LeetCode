# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSymmetricHelper(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            if left.val == right.val:
                return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)
            else:
                return False
        return root is None or isSymmetricHelper(root.left, root.right)
        
