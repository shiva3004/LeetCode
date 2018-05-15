   def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 0
        rear = front = None
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        temp = head
        while temp:
            count += 1
            if m == count:
                rear = temp
            if n+1 == count:
                front = temp
            if rear and front:
                rear.next = self.reverse(rear.next, front)
            temp = temp.next
        return head.next
    
    def reverse(self,rear, front):
        curr = rear
        prev = front.next
        front =  front.next
        while curr != front:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        return prev
