# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        fast = slow = head
        while fast is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
            if fast is None or fast.next is None or fast.next.next is None:
                break
        return False
