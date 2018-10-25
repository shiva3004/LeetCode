class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr = [ i for i in range(n + 1)]
        
        return self.getPermutationHelper(arr, n, k)
    
    def getPermutationHelper(self, arr, n, k):
        if n == 1:
            return str(arr[-1])
        
        total = math.factorial(n)
        each = math.factorial(n-1)
        number = total // each
        index = 0
        for i in range(1, n + 1):
            if i * each >= k:
                index = i
                break
        
        res = str(arr[index])
        arr = arr[:index] + arr[index + 1:]
        n -= 1
        k -= (index - 1) * each
        
        res += self.getPermutationHelper(arr, n, k)
        
        return res
        
