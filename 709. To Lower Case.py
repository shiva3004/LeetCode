class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = []
        for i in range(len(str)):
            if 65 <= ord(str[i]) <= 90: 
                res.append(chr(ord(str[i]) + 32))
            else:
                res.append(str[i])
        return ''.join(res)
                
        
