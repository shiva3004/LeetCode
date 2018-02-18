# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        l = [] * k
        count = 0
        tail = root
        while tail is not None:
            tail = tail.next
            count += 1
        size, rem = divmod(count, k)
        print(size, rem)
        tail = root
        while tail is not None:
            l.append(tail)
            if size == 0:
                if rem > 0:
                    rem -= 1
            else:
                for i in range(size - 1):
                    tail = tail.next
                    print(1)
                if rem > 0:
                    tail = tail.next
                    rem -= 1
            temp = tail.next
            tail.next = None
            tail = temp    
        for i in range(k - len(l)):
            l.append([])
        return l
