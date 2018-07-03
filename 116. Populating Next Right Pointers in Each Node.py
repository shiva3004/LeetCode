# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        parent = collections.deque()
        parent.append(root)
        while len(parent) > 0:
            children = collections.deque()
            prev = None
            while len(parent) > 0:
                p = parent.popleft()
                if p is None:
                    return
                children.append(p.left)
                children.append(p.right)
                if prev is None:
                    prev = p
                elif p:
                    prev.next = p
                    prev = p
            parent = children
