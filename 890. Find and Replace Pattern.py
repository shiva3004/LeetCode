class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            if self.isReplacement(pattern, word):
                res.append(word)
        return res
    
    def isReplacement(self, pattern, word):
        map1 = {}; map2 = {}
        
        if len(pattern) != len(word):
            return False
        
        for i in range(len(pattern)):
            p = pattern[i]; w = word[i]
            
            if p not in map1:
                map1[p] = w
            elif w != map1[p]:
                return False
            
            if w not in map2:
                map2[w] = p
            elif p != map2[w]:
                return False
            
        return True
              
