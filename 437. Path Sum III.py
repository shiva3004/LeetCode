# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.pathSumHelper(root, sum)[1]
    
    def pathSumHelper(self, root, sum):
        if root is None:
            return [[], 0]
        
        left = self.pathSumHelper(root.left, sum)
        right = self.pathSumHelper(root.right, sum)
        res = []
        count = left[1] + right[1]
        total = left[0] + right[0]
        #print(total)
        for val in total:
            if val + root.val == sum:
                count += 1
            res.append(val + root.val)
        if root.val == sum:
            count += 1
        res.append(root.val)
    
        return [res, count]
    
