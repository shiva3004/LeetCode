# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxAncestorDiffHelper(root, root.val, root.val)
    
    def maxAncestorDiffHelper(self, root, minVal, maxVal):
        if root is None:
            return 0
        res = max(abs(root.val - maxVal), abs(root.val - minVal))
        lres = self.maxAncestorDiffHelper(root.left, min(minVal, root.val), max(maxVal, root.val))
        rres = self.maxAncestorDiffHelper(root.right, min(minVal, root.val), max(maxVal, root.val))
        return max(res, lres, rres)
