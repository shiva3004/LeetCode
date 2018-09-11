class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(pattern) != len(str):
            return False
        word_mapper = {}
        
        for i in range(len(pattern)):
            if pattern[i] in word_mapper:
                if word_mapper[pattern[i]] != str[i]:
                    return False
            elif str[i] in word_mapper.values():
                return False
            else:
                word_mapper[pattern[i]] = str[i]
        return True
