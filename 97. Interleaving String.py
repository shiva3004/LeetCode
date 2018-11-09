class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        def isInterleaveHelper(s1, s2, s3, i, j, k, memory):
            t_i = i; t_j = j
            if i == len(s1):
                t_i = i - 1
            if j == len(s2):
                t_j = j - 1
            if memory[t_i][t_j] is not None:
                return memory[t_i][t_j]
            
            if i == len(s1) and j == len(s2) and k == len(s3):
                memory[i-1][j-1] = True
                return memory[i-1][j-1]
            elif len(s3) == k:
                memory[t_][t_j] = False
                return memory[t_i][t_j]
            
            if i < len(s1)  and s1[i] == s3[k]:
                if isInterleaveHelper(s1, s2, s3, i + 1, j, k + 1, memory):
                    memory[t_i][t_j] = True
                    return memory[t_i][t_j]
                
            if j < len(s2) and s2[j] == s3[k]:
                if isInterleaveHelper(s1, s2, s3, i, j + 1, k + 1, memory):
                    memory[t_i][t_j] = True
                    return memory[t_i][t_j]
                
            memory[t_i][t_j] = False
            return memory[t_i][t_j]
        
        i = 0; j = 0; k = 0
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == len(s2) == len(s3) == 0:
            return True
        elif len(s1) == 0:
            return s2 == s3
        elif len(s2) == 0:
            return s1 == s3
        memory = [[None for j in range(len(s2))] for i in range(len(s1))]
        return isInterleaveHelper(s1, s2, s3, i, j, k , memory)
