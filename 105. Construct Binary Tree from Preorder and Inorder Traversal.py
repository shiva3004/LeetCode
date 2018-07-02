# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        vars = {'index': 0}
        def buildTree(inorder):
            if len(inorder) < 1:
                return None
            root = TreeNode(preorder[vars['index']])
            index = inorder.index(preorder[vars['index'] ])
            vars['index'] += 1
            root.left = buildTree(inorder[:index])
            root.right = buildTree(inorder[index+1:])
            return root
        return buildTree(inorder)
