# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        curr = head
        count = 0
        G = set(G)
        while curr:
            if curr.val in G:
                count += 1
                curr = curr.next
                while curr:
                    if curr.val not in G:
                        break
                    curr = curr.next
            curr = curr.next if curr else curr
        return count
