class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def combineHelper(rem, arr, k):
            if len(rem) == k:
                res.append(rem[:])
                return
            if len(arr) == 0:
                return
            for i in range(len(arr)):
                rem.append(arr[i])
                combineHelper(rem, arr[i+1:], k)
                if rem:
                    rem.pop()
        combineHelper([],[i for i in range(1, n+1)], k)
        return res
            
