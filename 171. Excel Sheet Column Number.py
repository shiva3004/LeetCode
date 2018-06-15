class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        for i in range(len(s)):
            n = ord(s[i]) - 64
            val += n * (26**(len(s)-i-1))
        return val
        
