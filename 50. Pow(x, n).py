class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not -2147483648 < n < 2147483647:
            return 0
        res = x
        for i in xrange(1,abs(n)):
            res *= x
        if n < 0:
            return 1/res if n%2 ==0 or 0 < x < 1  else -(1/res)
        return abs(res) if n%2 == 0 else res
        
