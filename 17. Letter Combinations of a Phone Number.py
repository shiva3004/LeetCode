class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        v = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if digits == "":
            return []
        elif len(digits) == 1:
            ans = [x for x in v[int(digits[0])]]
            return ans
        a = v[int(digits[0])]
        for i in range(len(digits)-1):
            a = self.get_permutations(a, v[int(digits[i+1])])
        return a
    
    def get_permutations(self, a, b):
        ans = []
        for i in range(len(a)):
            for j in range(len(b)):
                ans.append(a[i]+b[j])
        return ans
