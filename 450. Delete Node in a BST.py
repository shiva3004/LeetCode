# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def findMin(root):
            if root.left is None:
                return root.val
            return findMin(root.left)
        if root is None:
            return root
        if root.val == key:
            if root.left and root.right:
                root.val = findMin(root.right)
                root.right = self.deleteNode(root.right, root.val)
                return root
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
        
