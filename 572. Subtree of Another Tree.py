class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        if s.val == t.val:
            if self.isSubtreeHelper(s, t):
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSubtreeHelper(self, s, t):
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        if s.val == t.val:
            return self.isSubtreeHelper(s.left, t.left) and self.isSubtreeHelper(s.right, t.right)
            
