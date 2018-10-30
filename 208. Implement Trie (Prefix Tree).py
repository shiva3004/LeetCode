class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = None
        self.children = {}
        self.isWord = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        #print(word)
        if len(word) == 0:
            return
        if word[0] not in self.children:
            self.children[word[0]] = [Trie(), False]
            self.insertHelper(word[1:], self.children[word[0]][0])
        else:
            self.insertHelper(word[1:], self.children[word[0]][0])
        
        if len(word) == 1:
            self.children[word[0]][1] = True
        
    def insertHelper(self, word, trie):
        if len(word) == 0:
            return
        
        if word[0] not in trie.children:
            trie.children[word[0]] = [Trie(), False]
            #print(trie.children[word[0]])
            trie.insertHelper(word[1:], trie.children[word[0]][0])
        else:
            trie.insertHelper(word[1:], trie.children[word[0]][0])
        
        if len(word) == 1:
            trie.children[word[0]][1] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(word) == 1 and word[0] in self.children and self.children[word[0]][1]:
            return True
        elif len(word) == 0:
            return False
        
        if word[0] in self.children:
            return self.searchHelper(word[1:], self.children[word[0]][0])
        else:
            return False
    
    def searchHelper(self, word, trie):
        if len(word) == 1 and word[0] in trie.children and trie.children[word[0]][1]:
            return True
        elif len(word) == 0:
            return False
        
        if word[0] in trie.children:
            return trie.searchHelper(word[1:], trie.children[word[0]][0])
        else:
            return False
    
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) == 0:
            return False
        if prefix[0] in self.children:
            return self.startsWithHelper(prefix[1:], self.children[prefix[0]][0])
        else:
            return False
    
    def startsWithHelper(self, prefix, trie):
        if len(prefix) == 0:
            return True
        
        if prefix[0] in trie.children:
            return trie.startsWithHelper(prefix[1:], trie.children[prefix[0]][0])
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
