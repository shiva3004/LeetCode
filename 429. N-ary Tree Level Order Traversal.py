"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        parent = [root]
        while parent:
            leaves = []
            vals = []
            while parent:
                p = parent.pop()
                for child in p.children:
                    if child:
                        leaves.append(child)
                vals.append(p.val)
            parent = leaves[::-1]
            res.append(vals)
        return res
                
                    
                    
