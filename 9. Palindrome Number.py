class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0):
            return False
        for i in range(len(str(x))):
            if str(x)[i] != str(x)[-(i+1)]:
                print(str(x)[i],str(x)[-(i+1)])
                return False
        return True
