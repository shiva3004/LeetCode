# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def getNode(root):
            while root.right:
                root = root.right
            return root
        if root is None:
            return root
        if root.left is not None:
            temp = root.right
            root.right = root.left
            root.left = None
            last = getNode(root.right)
            last.right = temp
        self.flatten(root.right)
