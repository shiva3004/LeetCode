# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        left_array_index = self.getLeftArray(preorder)
        right_array_index = self.getLeftArray(preorder)
        
        if left_array_index == -1:
            left_array = []
        else:
            left_array = preorder[1: left_array_index]
        
        if right_array_index == -1:
            right_array = []
        else:
            right_array = preorder[right_array_index: ]
            
        root.left = self.bstFromPreorder(left_array)
        root.right = self.bstFromPreorder(right_array)
        
        return root
    
    def getLeftArray(self, preorder):
        if len(preorder) == 0:
            return -1
        parent = preorder[0]
        for i in range(1, len(preorder)):
            if parent < preorder[i]:
                return i
        return len(preorder)
