# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head is None or head.next is None:
            return head
        n = 0
        tail = head
        while tail:
            n += 1
            tail = tail.next
        k = k % n
        if k == 0:
            return head
        tail = head
        for i in range(n-k-1):
            tail = tail.next
        h_temp = tail.next
        tail.next = None
        temp = head
        head = h_temp
        while h_temp.next:
            h_temp = h_temp.next
        h_temp.next = temp
        return head
