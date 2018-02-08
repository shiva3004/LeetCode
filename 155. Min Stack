class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_list = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min_list) == 0:
            self.min_list.append(x)
        elif x <= self.getMin():
            self.min_list.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return None
        x = self.stack.pop()
        print 2
        if x == self.min_list[-1]:
            print 3
            min = self.min_list.pop()
        return x
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """ 
        print self.min_list[-1]
        return self.min_list[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
