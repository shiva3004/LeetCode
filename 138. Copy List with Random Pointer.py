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
        if head is None:
            return head
        node_dictionary = {}
        tail = head
        while tail:
            node_dictionary[tail] = RandomListNode(tail.label)
            tail = tail.next
        tail = head
        while tail:
            if tail.next:
                node_dictionary[tail].next = node_dictionary[tail.next]
            if tail.random:
                node_dictionary[tail].random = node_dictionary[tail.random]
            tail = tail.next
        return node_dictionary[head]
