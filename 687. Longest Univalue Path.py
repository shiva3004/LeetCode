# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_val = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.longestUnivalPath(root)
        return self.max_val
    
    def longestUnivalPath(self, root):
        if root is None:
            return [0, None]
        
        tot_len = 0
        left_len, left_val =  self.longestUnivalPath(root.left)
        right_len, right_val = self.longestUnivalPath(root.right)
        # print('l',left_len, left_val)
        # print('r',right_len, right_val)
        if left_val is not None and left_val == root.val:
            tot_len += left_len + 1
            left_len += 1
        else:
            left_len = 0
        
        if right_val is not None and right_val == root.val:
            tot_len += right_len + 1
            right_len += 1
        else:
            right_len = 0
        #print(root.val, tot_len)
        if tot_len > self.max_val:
            self.max_val = tot_len
        
        return [max(left_len, right_len), root.val]
        
