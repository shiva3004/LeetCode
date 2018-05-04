class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split('/')
        res = []
        for p in paths:
            if p == '.' or p == '':
                pass
            elif p == '..':
                if len(res) == 0:
                    pass
                else:
                    res.pop()
            else:
                res.append('/'+p)
        if len(res) == 0:
            return '/'
        return ''.join(res)
                
