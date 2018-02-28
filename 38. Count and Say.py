class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            s = self.convert_count_string(s)
            print(i, s)
        return s
        
    def convert_count_string(self, n):
        count = 0
        temp = []
        if len(n) == 1:
            return '11'
        for i in range(len(n)-1):
            if n[i] != n[i+1]:
                temp.append(count + 1)
                temp.append(n[i])
                count = 0
            else:
                count += 1
            if i+2 == len(n):
                if n[i] == n[i+1]:
                    temp.append(count+1)
                    temp.append(n[i])
                else:
                    temp.append(1)
                    temp.append(n[i+1])
        return ''.join(str(t) for t in temp)
