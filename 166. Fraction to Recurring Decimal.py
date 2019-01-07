class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        dec = ''
        if numerator == 0:
            return '0'
        if denominator == 0:
            return 'NaN'
        if numerator < 0 and denominator < 0:
            pass
        elif numerator < 0 or denominator < 0:
            dec = '-'
            numerator = abs(numerator); denominator = abs(denominator)
        dec += str(numerator // denominator)
        frc = []; res = ''
        rem = numerator % denominator
        if rem == 0:
            return dec
        org_rem = [rem]
    
        while True:
            val = rem * 10
            frc.append(str(val // denominator))
            rem = val % denominator
            for k in range(len(org_rem)):
                if org_rem[k] == rem:
                    index = k
                    return dec + '.' + ''.join(frc[:index]) + '(' +  ''.join(frc[index:]) + ')'
            if rem == 0:
                break
            org_rem.append(rem)
             
        return dec + '.' + ''.join(frc)
