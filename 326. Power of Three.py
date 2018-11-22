class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        val = 1
        while val <= n:
            if val == n:
                return True
            val *= 3
        return False
