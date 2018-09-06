# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def sumNumbers(root, val):
            if root is None:
                return
            if root.left is None and root.right is None:
                res.append(int(val+str(root.val))) 
                return
            sumNumbers(root.left, val + str(root.val))
            sumNumbers(root.right, val + str(root.val))
        sumNumbers(root, '0')
        return sum(res)
