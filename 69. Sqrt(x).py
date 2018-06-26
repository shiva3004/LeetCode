class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x
        if x < 2:
            return x
        while start + 1 < end:
            mid = (start+end)//2
            if mid * mid < x:
                start = mid
            elif mid*mid > x:
                end = mid
            else:
                return mid
        return start
        
