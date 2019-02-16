# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        current = 0; previous = 0
        self.rightSideViewHelper(root, current, previous)
        return self.ans
    
    def rightSideViewHelper(self, root, current, previous):
        if root is None:
            return current - 1
        if current == previous == 0 or current > previous:
            self.ans.append(root.val)
        previous = max(self.rightSideViewHelper(root.right, current + 1, previous), previous)
        previous = max(self.rightSideViewHelper(root.left, current + 1, previous), previous)
        return previous
