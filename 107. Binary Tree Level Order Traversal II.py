# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        def levelOrderBottom(root, index):
            if root is None:
                return
            if index > len(result)-1:
                result.append([])
            result[index].append(root.val)
            levelOrderBottom(root.left, index+1)
            levelOrderBottom(root.right, index+1)
        levelOrderBottom(root, 0)
        return result[::-1]
