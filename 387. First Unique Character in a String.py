class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha_s = {}
        
        for i in range(len(s)):
            if s[i] not in alpha_s:
                alpha_s[s[i]]  = 1
            else:
                alpha_s[s[i]] += 1
        for i in range(len(s)):
            if alpha_s[s[i]] == 1:
                return i
        return -1
