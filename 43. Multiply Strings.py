class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        mul = []
        max_len = 0
        if num1 == '0' or num2 == '0':
            return '0'
        for i in range(len(num1)):
            a = int(num1[-(i+1)])
            add = []
            carry = 0
            for k in range(i):
                add.append(0)
            for j in range(len(num2)):
                b = int(num2[-(j+1)])
                val = a * b
                if carry > 0:
                    val += carry
                val, carry = val%10, val/10
                add.insert(0,val)
            if carry > 0:
                add.insert(0,carry)
            if len(add) > max_len:
                max_len = len(add)
            mul.append(add)
        res = []
        carry = 0
        for i in range(max_len):
            val = 0
            if carry > 0:
                    val += carry
            for arr in mul:
                val += arr.pop() if len(arr) > 0 else 0
            val, carry = val%10, val/10
            res.insert(0,str(val))
        if carry > 0:
            res.insert(0, str(carry))
        return ''.join(res)
