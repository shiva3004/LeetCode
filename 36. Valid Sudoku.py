class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """       
        for i in range(3):
            t = []
            for j in range(3):
                t = []
                t.append(board[3*i:3*i+3][0][3*j:3*j+3])
                t.append(board[3*i:3*i+3][1][3*j:3*j+3])
                t.append(board[3*i:3*i+3][2][3*j:3*j+3])
                if not self.is_valid(t):
                    return False
         
        for l in board:
            if not self.is_valid(l):
                return False
        
        for i in range(9):
            t = set([])
            for l in board:
                if l[i] in t and l[i] != '.':
                    return False
                else:
                    t.add(l[i])
        return True
    
    def is_valid(self, b):
        t = set([])
        for l in b:
            for i in range(len(l)):
                if l[i] in t and l[i] != '.':
                    return False
                else:
                    t.add(l[i])
        return True
            
