class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = 0
        values = set([])
        values.add(n)
        while n > 0:
            val = n % 10
            temp += val * val
            n /= 10
            #print(temp, val)
            if n == 0:
                #print('#', temp)
                n = temp
                temp = 0
                if n == 1:
                    return True
                elif n in values:
                    return False
                values.add(n)
