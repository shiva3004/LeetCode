class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        min_val = A[0]
        for i in range(len(A)):
            if min_val >= A[i]:
                min_val = A[i]
                min_index = i
        if min_index == len(A) - 1:
            return 1
        max_in_left = max(A[:min_index+1])
        #print(max_in_left)
        left = 0
        max_val = A[0]
        for i in range(len(A)):
            if A[i] < max_in_left:
                left = i
                max_in_left = max(max_in_left, A[i], max_val)
            max_val = max(max_in_left, A[i], max_val)
        return left + 1
            
