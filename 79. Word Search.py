class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def getAdjacents(board, memory, i, j):
            res = []
            s_i = i if i == 0 else i - 1
            e_i = i if i == len(board)-1 else i+1
            while s_i <= e_i:
                if s_i != i and memory[s_i][j] == 0:
                    res.append([s_i, j])
                s_i += 1
            s_j = j if j == 0 else j-1
            e_j = j if j == len(board[0])-1 else j+1
            while s_j <= e_j:
                if s_j != j and memory[i][s_j] == 0:
                    res.append([i, s_j])
                s_j += 1
            return res
        
        def exist(board, word, i, j):
            if len(word) == 0:
                return True
            adj_s = getAdjacents(board,memory, i, j)
            for adj in adj_s:
                i = adj[0]
                j = adj[1]
                if word[0] == board[i][j]:
                    memory[i][j] = 1
                    if exist(board, word[1:], i, j):
                        return True
                    memory[i][j] = 0
            return False
        
        if len(word) == 0:
                return True
        memory = [ [0 for i in range(len(board[0])) ] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    memory[i][j] = 1
                    if exist(board, word[1:], i, j):
                        return True
                    memory[i][j] = 0
        return False
    
        
    
        
