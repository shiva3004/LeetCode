class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            a = s[i].lower()
            b = s[j].lower()
            if ('a' <= a <= 'z' or '0' <= a <= '9') and ('a' <= b <= 'z' or '0' <= b <= '9'):
                if a != b:
                    return False
                else:
                    i += 1
                    j -= 1
            elif not ('a' <= a <= 'z' or '0' <= a <= '9'):
                i += 1
            elif not ('a' <= b <= 'z' or '0' <= b <= '9'):
                j -= 1
        return True
