class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """ 
        def getValues(a, b, carry):
            val = int(a)+ int(b)+ carry
            if val == 0:
                res.append('0')
                return 0
            elif val == 1:
                res.append('1')
                return 0
            elif val == 2:
                res.append('0')
                return 1
            elif val == 3:
                res.append('1')
                return 1
            
        a = a[::-1]
        b = b[::-1]
        if len(a) < len(b):
            for i in range(len(b)-len(a)):
                a += '0'
        else:
            for i in range(len(a)-len(b)):
                b += '0'
        carry = 0
        res = []
        for i in range(len(b)):
            carry = getValues(a[i], b[i] , carry)
        if carry:
            res.append('1')
        return ''.join(res)[::-1]
