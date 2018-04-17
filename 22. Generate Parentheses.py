class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = self.generateParenthesisHelper(n)
        if n == 0:
            return ['']
        return list(res)
    
    def generateParenthesisHelper(self,n):
        if n == 1:
            return ['()']
        params = self.generateParenthesisHelper(n-1)
        res_params = set([])
        
        for strg in params:
            for i in range(len(strg)):
                if strg[i] == '(' :
                    res_params.add(strg[:i+1] + '()' + strg[i+1:])
            res_params.add('()'+strg)
        return res_params
