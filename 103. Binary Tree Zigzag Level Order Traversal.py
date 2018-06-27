# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        parent = collections.deque()
        parent.append(root)
        res = []
        change_order = True
        while len(parent) > 0:
            temp = []
            children = collections.deque()
            while len(parent) > 0:
                p = parent.popleft()
                if p:
                    children.append(p.left)
                    children.append(p.right)
                    temp.append(p.val)
            if change_order:
                res.append(temp)
                change_order = False
            else:
                res.append(temp[::-1])
                change_order = True
            parent = children
        return res[:-1]
        
