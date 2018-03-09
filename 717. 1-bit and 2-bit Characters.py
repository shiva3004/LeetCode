class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) -2:
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1 and (bits[i+1] == 1 or bits[i+1] == 0):
                i += 2
        return bits[i] == 0
                
        
