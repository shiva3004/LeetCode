class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) > 0:
            return self.remValid(word, 'A', 'Z') or self.remValid(word[1:], 'a', 'z')
    
    def remValid(self, word, start, end):
        for c in word:
            if start <= c <= end:
                pass
            else:
                return False
        return True
        
