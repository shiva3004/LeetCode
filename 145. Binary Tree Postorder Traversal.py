# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root]
        res = []
        seen = set([None])
        node = root
        while len(stack) > 0:
            node = stack[-1]
            if (node.left is None and node.right is None) or (node.left in seen and node.right in seen):
                seen.add(node)
                res.append(node.val)
                stack.pop()
            if node.right and node.right not in seen:
                stack.append(node.right)
            if node.left and node.left not in seen:
                stack.append(node.left)
            
        return res
