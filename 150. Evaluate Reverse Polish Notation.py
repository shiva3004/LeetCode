class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        exp = []
        operator = '+-*/'
        for each in tokens:
            if each not in operator:
                exp.append(int(each))
            else:
                val1 = exp.pop()
                val2 = exp.pop()
                if each == '+':                    
                    val = val1 + val2
                elif each == '-':                    
                    val = val2 - val1
                elif each == '/':                    
                    val = int(val2 / val1)
                elif each == '*':                    
                    val = val1 * val2
                exp.append(val)
        return exp[0]
        
