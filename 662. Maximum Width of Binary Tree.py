# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        queue = [[root, 0, 0]]
        left = right = cur_depth = 0
        for node, right, depth in queue:
            if node:
                queue.append([node.left, right*2, depth + 1])
                queue.append([node.right, right*2 + 1, depth + 1])
                if cur_depth != depth:
                    cur_depth = depth
                    left = right
                ans = max(right - left + 1, ans)
        return ans
                
