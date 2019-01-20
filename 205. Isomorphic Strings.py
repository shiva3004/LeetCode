class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapper = collections.defaultdict()
        for i in range(len(s)):
            a = s[i]; b = t[i]
            if a not in mapper:
                if b in mapper.values():
                    return False
                mapper[a] = b
            else:
                if mapper[a] != b:
                    return False
        return True
        
