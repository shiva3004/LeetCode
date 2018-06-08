# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        parent = collections.deque()
        parent.append(root)
        result = []
        while len(parent) > 0:
            children = collections.deque()
            temp = []
            while len(parent) > 0:
                p = parent.popleft()
                if p:
                    children.append(p.left)
                    children.append(p.right)
                    temp.append(p.val)
            result.append(temp)
            parent = children
        return result[:-1]
                    
            
