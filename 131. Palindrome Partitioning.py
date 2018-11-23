class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(1, len(s)):
            if self.isPalindrome(s[:i]):
                first = s[:i]
                ret_palins = self.partition(s[i:])
                for palins in ret_palins:
                    res.append([first] + palins)
        if self.isPalindrome(s):
            res.append([s])
        return res
        
    def isPalindrome(self, s):
        return s == s[::-1]
