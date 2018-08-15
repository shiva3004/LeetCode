# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        x = {'header': head}
        
        def sortedListToBSTHelper(start, end):
            if start > end:
                return None
            mid = (start+end) // 2
            left = sortedListToBSTHelper(start, mid-1)
            node = TreeNode(x['header'].val)
            node.left = left

            x['header'] = x['header'].next
            right = sortedListToBSTHelper(mid+1, end)
            node.right = right
            return node
        
        runner = head
        size = 0
        while runner:
            runner = runner.next
            size += 1
        end = size
        start = 0
        return sortedListToBSTHelper(start, end-1)
        
        
