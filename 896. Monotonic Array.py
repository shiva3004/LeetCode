class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        mon_inc = None
        mon_dec = None
        for i in range(1, len(A)):
            if not mon_inc and A[i-1] < A[i]:
                mon_inc = True
            if mon_inc and A[i-1] > A[i]:
                return False
        
        
        
        for i in range(1, len(A)):
            if not mon_dec and A[i-1] > A[i]:
                mon_dec = True
            if mon_dec and A[i-1] < A[i]:
                return False
        
        return True
             
