class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        map1 = [0 for i in range(26)]; map2 = [ 0 for i in range(26)]
        res = []
        for b in B:
            map2 = self.count(b)
            map1 = self.merge(map1, map2)
    
        for a in A:
            map2 = self.count(a)
            if self.isSubset(map1, map2):
                res.append(a)
        return res
    
    def isSubset(self, map1, map2):
        for i in range(26):
            if map1[i] > map2[i]:
                return False
        return True
        
    
    def merge(self, map1, map2):
        for i in range(26):
            map1[i] = max(map1[i], map2[i])
        return map1
    
    def count(self, word):
        mapper = [0 for i in range(26)]
        for letter in word:
            mapper[ord(letter) - ord('a')] += 1
        return mapper
        
        
