class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 26:
            return chr(64 + n)
        val = (n - 1) // 26
        return self.convertToTitle(val) + chr(64 + (n - 26 * val))
