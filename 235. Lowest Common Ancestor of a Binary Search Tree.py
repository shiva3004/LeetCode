# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if p.val > q.val:
        #     temp = p
        #     p = q
        #     q = temp
        return self.find_lca(root, p ,q)
        
    def find_lca(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.find_lca(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.find_lca(root.right, p, q)
        else:
            return root
