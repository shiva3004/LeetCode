class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        stack = []
        while i < len(s):
            if s[i] == ')' and len(stack) > 0:
                exp = []
                j = i
                while stack[-1] != '(':
                    exp.append(stack.pop())
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                res = self.convertToExp(exp[::-1])
                stack.append(res)
                i += 1
            elif s[i] == ' ':
                i += 1
                continue
            else:
                num = ''
                if s[i].isdigit():
                    while i < len(s) and s[i].isdigit():
                        num += s[i]
                        i += 1
                    stack.append(int(num))
                else:
                    stack.append(s[i])
                    i += 1
        return self.convertToExp(stack)
    
    def convertToExp(self, exp):
        i = 0; res = 0
        while i < len(exp):
            if exp[i] == '+':
                res += exp[i+1]
                i += 1
            elif exp[i] == '-':
                res -= exp[i+1]
                i += 1
            else:
                res += exp[i]
            i += 1
        return res
                
        
            
