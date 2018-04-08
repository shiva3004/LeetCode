# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or  head.next is None:
            return head
        a = head
        b = head.next
        p = head
        head = b
        while b:
            n = b.next
            b.next = a
            a.next = n
            if n is None or n.next is None:
                break
            a = n
            b = a.next
            p.next = b
            p = a
        return head
