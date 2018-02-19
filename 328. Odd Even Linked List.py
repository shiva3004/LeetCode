# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t_o_list = o_list = ListNode(0)
        t_e_list = e_list = ListNode(0)
        odd = True
        tail = head
        while tail is not None:
            if odd:
                t_o_list.next = tail
                tail = tail.next
                t_o_list = t_o_list.next
                t_o_list.next = None
                odd = False
            else:
                t_e_list.next = tail
                tail = tail.next
                t_e_list = t_e_list.next
                t_e_list.next = None
                odd = True
        t_o_list.next = e_list.next
        return o_list.next
