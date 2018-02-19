# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        if not (fast and fast.next and fast.next.next):
            return None
        slow = head
        while slow is not None:
            if slow is fast:
                return slow
            slow = slow.next
            fast = fast.next
        
