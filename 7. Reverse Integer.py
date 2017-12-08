class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        val = 0
        if x > 0:
            while x > 0:
                val = val*10 + x%10
                x = x/10
        else:
            x *= -1
            while x > 0:
                val = val*10 + x%10
                x = x/10
            val *= -1
        if abs(val) > 2147483647:
            return 0
        return val
