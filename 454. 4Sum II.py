class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        h_map1 = {}
        h_map2 = {}
        count = 0
        for i in range(len(A)):
            for j in range(len(B)):
                h_map1[A[i] + B[j]] = h_map1.get(A[i] + B[j], 0) + 1
    
        for i in range(len(C)):
            for j in range(len(D)):
                h_map2[-(C[i] + D[j])] = h_map2.get(-(C[i] + D[j]), 0) + 1
        
        for key in h_map1:
            if key in h_map2:
                count += h_map1[key] * h_map2[key]
            
        return count
