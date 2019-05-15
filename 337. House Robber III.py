# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mapper = {}
        return self.robHelper(root, mapper)
    
    def robHelper(self, root, mapper):
        if root is None:
            return 0
        if root in mapper:
            return mapper[root]
        val = 0
        if root.left:
            val += self.robHelper(root.left.left, mapper) + self.robHelper(root.left.right, mapper)
        if root.right:
            val += self.robHelper(root.right.left, mapper) + self.robHelper(root.right.right, mapper)
        mapper[root] = max(root.val + val, self.robHelper(root.left, mapper) + self.robHelper(root.right, mapper))
        return mapper[root]
