# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        tail = prev = head
        while tail is not None:
            if tail.val == val:
                if tail == head:
                    head = head.next
                    tail = head
                else:
                    prev.next = tail.next
                    tail = tail.next
            else:
                prev = tail
                tail = tail.next
        return head
