class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for c in s:
            if c == ']':
                popped = ''
                sub = ''
                while stack[-1] != '[':
                    popped += stack.pop()
                stack.pop()
                num = ''
                while len(stack) > 0 and stack[-1].isdigit():
                    num += stack.pop()
                popped = popped[::-1]
                num = num[::-1]
                for i in range(int(num)):
                    sub += popped
                for k in sub:
                    stack.append(k)
            else:
                stack.append(c)
        return ''.join(stack)
