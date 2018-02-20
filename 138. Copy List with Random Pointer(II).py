# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        tail = head
        dup_head = dup_tail = None
        while tail:
            dup = RandomListNode(tail.label)
            temp = tail.next
            tail.next = dup
            dup.next = temp
            tail = temp
        tail = head
        while tail:
            if tail.random:
                tail.next.random = tail.random.next
            tail = tail.next.next   
        tail = head
        while tail:
            if dup_tail is None:
                dup_tail = dup_head = tail.next
            else:
                dup_tail.next = tail.next
                dup_tail = dup_tail.next
            tail.next = tail.next.next
            tail = tail.next
        return dup_head
        
