# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        fast = slow = head
        rev_h = None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow
        slow = slow.next
        temp.next = None
        if fast.next:
            fast = fast.next
        while slow:
            temp = slow
            slow = slow.next
            if rev_h is None:
                rev_h = temp
                rev_h.next = None
            else:
                temp.next = rev_h
                rev_h = temp
        tail = head
        while rev_h:
            temp = rev_h
            rev_h = rev_h.next
            temp.next = tail.next
            tail.next = temp
            tail = temp.next
        
