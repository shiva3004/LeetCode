# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        parent = [root]
        while parent:
            val = 0.0
            count = 0
            children = []
            while parent:
                p = parent.pop()
                val += p.val
                count += 1
                if p.left:
                    children.append(p.left)
                if p.right:
                    children.append(p.right)
            res.append(val / count)
            parent = children
        return res
                
        
