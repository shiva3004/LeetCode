class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if s[-(i+1)] == ' ' and count > 0 :
                return count
            elif s[-(i+1)] != ' ':
                count += 1
        return count
