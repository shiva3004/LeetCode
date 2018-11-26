class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        t = collections.defaultdict(int)
        res = [ 0  for i in range(len(T))]
        for i in range(len(T)-1, -1, -1):
            temp = T[i]
            j = self.getMaxIndex(t, temp, i)
            res[i] = j - i
            t[temp] = min(i, j)
        return res
        
    def getMaxIndex(self, t, temp, i):
        min_val = float('inf')
        for key in t:
            if key > temp:
                min_val = min(t[key], min_val)
        if min_val == float('inf'):
            min_val = i
        return min_val
