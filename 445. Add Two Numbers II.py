# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        
        temp = l1
        while temp:
            s1.append(temp.val)
            temp = temp.next
            
        temp = l2
        while temp:
            s2.append(temp.val)
            temp = temp.next
        
        carry = 0
        head = None
        prev = None
        s1, s2 = [s1, s2] if len(s1) > len(s2) else [s2, s1]
        
        while len(s1) > 0:
            val = s1.pop() + (s2.pop() if len(s2) > 0 else 0) + carry
            #print(divmod(val, 10))
            carry, val = divmod(val, 10)
            head = ListNode(val)
            head.next = prev
            prev = head
            #print(head.val)
        if carry > 0:
            head = ListNode(carry)
            head.next = prev
        return head
            
        
