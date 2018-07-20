class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def combinationSumHelper(candidates, target, val):
            if target == 0:
                res.append(val.copy())
                return
            if target < 0:
                return
            for i in range(len(candidates)):                
                val.append(candidates[i])
                combinationSumHelper(candidates[i:], target-candidates[i], val)
                val.pop()
        combinationSumHelper(candidates, target, [])
        return res
                                          
