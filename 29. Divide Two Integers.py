class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = False
        if dividend < 0 and divisor < 0:
            pass
        elif dividend < 0 or divisor < 0:
            neg = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if dividend == 0 or dividend < divisor:
            return 0
            
        res = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= temp << 1:
                temp = temp<< 1
                multiple = multiple<< 1
            res += multiple
            dividend -= temp
        if res >= pow(2,31):
            res =  pow(2,31)
            return -res if neg else res-1
        return -res if neg else res
