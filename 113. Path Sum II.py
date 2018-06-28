# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def pathSum_helper(root, sum_until, sum, arr):
            if root is None:
                return
            if sum_until + root.val == sum and root.left is None and root.right is None:
                arr.append(root.val)
                res.append(arr)
            pathSum_helper(root.left, sum_until+root.val,sum, arr + [root.val] )
            pathSum_helper(root.right, sum_until+root.val, sum, arr + [root.val])
        pathSum_helper(root, 0, sum, [])
        return res
