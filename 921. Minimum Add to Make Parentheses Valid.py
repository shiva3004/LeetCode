class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        count1 = 0
        count = 0
        for s in S:
            if s == '(':
                count += 1
            elif s == ')' and count == 0:
                count1 += 1
            else:
                count -= 1
        return count + count1
