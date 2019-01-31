class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = []
        while A > 0 or B > 0:
            if len(res) >= 2 and res[-1] == res[-2]:
                writeA = res[-1] == 'b'
            else:
                writeA = A > B
            if writeA:
                res.append('a')
                A -= 1
            else:
                res.append('b')
                B -= 1
        return ''.join(res)
                
