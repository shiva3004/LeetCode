class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I' : 1, 'V' : 5,
                  'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        prev = val = 0
        for i in range(1, len(s)+1):
            curr = roman[s[-i]]
            if prev <= curr:
                val += curr
            else:
                val -= curr
            prev = curr
        return val
