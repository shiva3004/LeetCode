# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def sortedArrayToBST(nums, left, right):
            if left > right:
                return None
            mid = (left+right+1)//2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums, left, mid-1)
            root.right = sortedArrayToBST(nums, mid+1, right)
            return root
        return sortedArrayToBST(nums, 0, len(nums)-1)
