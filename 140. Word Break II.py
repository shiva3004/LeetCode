class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memory = {}
        return self.wordBreakHelper(s, wordDict, memory)
    
    def wordBreakHelper(self, s, wordDict, memory):
        if s in memory:
            return memory[s]
        res = []
        if s == '':
            return ['']
        for i in range(1, len(s) + 1):
            word = s[:i]
            if word in wordDict:
                result = self.wordBreakHelper(s[i:], wordDict, memory)
                for a in result:
                    if a == '':
                        res.append(word)
                    else:
                        res.append(word + ' ' + a)
        memory[s] = res
        return memory[s]
                
                
