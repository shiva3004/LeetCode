class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        org_root = root
        def searchTree(root, val):
            if root is None:
                return False     
            #print(root.val, val)
            if root.val == val:
                #print('e', root.val, val)
                return True
            if root.val < val:
                return searchTree(root.right, val)
            else:
                return searchTree(root.left, val)
        def inOrder(root, k):
            if root is None:
                return False
            #print('in', root.val)
            if root.val > k - root.val:
                if searchTree(org_root, k-root.val):
                    return True
            else:
                if searchTree(root.right, k-root.val):
                    return True
            return inOrder(root.left, k) or inOrder(root.right, k)
        return inOrder(root, k) 
        
