class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        i = 0; res = 0
        while i < len(s):
            if s[i] in '*/':
                op = s[i]
                i += 1
                while i < len(s) and s[i] == ' ':
                    i += 1
                num1 = stack.pop()
                num2 = ''
                while i < len(s) and s[i].isdigit():
                    num2 += s[i]
                    i += 1
                res = self.evalExp(num1, op, int(num2))
                stack.append(res)
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
        
        i = 0; res = 0
        while i < len(stack):
            if stack[i] == '+':
                res += stack[i + 1]
                i += 1
            elif stack[i] == '-':
                res -= stack[i + 1]
                i += 1
            else:
                res += stack[i]
            i += 1
        
        return res
        
    def evalExp(self, num1, op, num2):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 // num2
                
