# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        memory = set([])
        l = []
        temp = head
        while temp:
            if temp.val in memory:
                l.append(temp.val)
            else:
                memory.add(temp.val)
            temp = temp.next
        
        temp = head
        prev_head = None
        print(l)
        while temp:
            if temp.val not in l:
                if prev_head is None:
                    prev_head = temp
                    prev = temp
                else:
                    prev.next = temp
                    prev = temp
                temp = temp.next
            else:
                temp = temp.next
        if prev_head:
            prev.next = None
        return prev_head
