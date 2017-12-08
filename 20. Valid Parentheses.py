class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        d = { '(' : ')',
            '[' : ']',
            '{' : '}'  
             }
        for each in s:
            if each in d.keys():
                arr.append(each)
            elif each in d.values():
                if len(arr) > 0:
                    symbol = arr.pop()
                    if d[symbol] == each:
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                return False
        return len(arr) == 0
