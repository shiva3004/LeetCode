class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        e = 0; o = 1
        while i < len(A):
            
            
            while e < len(A) and A[e] % 2 == 0:
                e += 2
            while o < len(A) and A[o] % 2 == 1:
                o += 2
            
            if e < len(A) and o < len(A):
                A[e], A[o] = A[o], A[e]
                
            i = min(o, e)
        return A
