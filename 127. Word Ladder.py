class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = [(beginWord, 0)]
        word_set = set(wordList)
        while queue:
            word, step = queue.pop(0)
            if word == endWord:
                return step + 1
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, step + 1))
        return 0
            
