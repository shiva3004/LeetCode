class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m1 = [ 0 for i in range(26)]
        m2 = [ 0 for i in range(26)]
        for c in s1:
            m1[ord(c) - ord('a')] += 1
        n = len(s1); i = 0; j = 0
        while j < len(s2):
            if j < n:
                m2[ord(s2[j]) - ord('a')] += 1
            else:
                if self.isSame(m1, m2):
                    return True
                m2[ord(s2[i]) - ord('a')] -= 1
                i += 1
                m2[ord(s2[j]) - ord('a')] += 1
            j += 1
        if self.isSame(m1, m2):
            return True
        return False
    
    def isSame(self, m1, m2):
        for i in range(26):
            if m1[i] != m2[i]:
                return False
        return True
