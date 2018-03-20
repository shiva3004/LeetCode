class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 or t2:
            ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
            ans.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
            ans.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
            return ans
