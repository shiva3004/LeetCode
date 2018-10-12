# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        runner = head
        size = 0
        while runner:
            runner = runner.next
            size += 1
        
        return self.sortList1(head, size)
    
    def sortList1(self, head, size):
        if head is None or head.next is None:
            return head
        mid = size // 2
        count = 0
        runner = head
        while count < mid-1:
            runner = runner.next
            count += 1
        prev = runner.next
       
        runner.next = None
        left = self.sortList1(head, mid)
        
        right = self.sortList1(prev, size - mid)
        
        r_head = None
        
        while left and right:
            if left.val < right.val:
                if r_head is None:
                    r_head = left
                    tail = r_head
                else:
                    tail.next = left
                    tail = tail.next
                left = left.next
            else:
                if r_head is None:
                    r_head = right
                    tail = r_head
                else:
                    tail.next = right
                    tail = tail.next
                right = right.next
        if left:
            tail.next = left
        elif right:
            tail.next = right
        
        return r_head
        
        
