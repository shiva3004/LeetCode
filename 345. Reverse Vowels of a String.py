class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = 'aeiouAEIOU'
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                temp = s[j]
                s[j] = s[i]
                s[i] = temp
                i += 1
                j -= 1
            elif s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
        return ''.join(s)
