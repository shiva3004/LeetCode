class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memory = [ None for i in range(len(s))]
        i = 0
        return self.wordBreakHelper(s, i, set(wordDict), memory) == True
    
    def wordBreakHelper(self, s, i, wordDict, memory):
        if i >= len(s):
            return True
        if memory[i] is not None:
            return memory[i]
        for j in range(i, len(s)+1):
            if s[i:j] in wordDict:
                memory[i] = (self.wordBreakHelper(s, j, wordDict, memory) == True)
                if memory[i]:
                    break
        return memory[i]
