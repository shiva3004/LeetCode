class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        val = inc = 1
        carry = 0
        for i in range(1, len(digits)+1):
            val += digits[-i] + carry
            carry = 0
            if val == 10:
                digits[-i] = 0 
                carry = 1
            else:
                digits[-i] += inc
                inc = 0
            val = 0
        if carry == 1:
            digits = [1] + digits
        return digits
        
