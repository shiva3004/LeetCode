class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        ni = 0; ti = 0
        
        while ti < len(typed):
            if ni == len(name):
                ni -= 1
            if len(name) > 0 and name[ni] == typed[ti]:
                ni += 1
                ti += 1
            else:
                if ti > 0 and typed[ti-1] == typed[ti]:
                    ti += 1
                else:
                    return False
        
        return ni == len(name)
