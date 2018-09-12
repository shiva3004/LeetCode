class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code_mapper = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                             ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                             "...","-","..-","...-",".--","-..-","-.--","--.."]
        memory = set([])
        for word in words:
            s = ''
            for i in range(len(word)):
                s += morse_code_mapper[ ord(word[i]) - 97 ]
            memory.add(s)
        return len(memory)
                

        
