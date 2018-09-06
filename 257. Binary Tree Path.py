# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def binaryTreePaths(root, val):
            if root is None:
                return
            if root.left is None and root.right is None:
                res.append(val+str(root.val))
                return
            binaryTreePaths(root.left, val+str(root.val)+'->')
            binaryTreePaths(root.right, val+str(root.val)+'->')
        binaryTreePaths(root, '')
        return res
