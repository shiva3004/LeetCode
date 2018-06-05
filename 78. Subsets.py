class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsetsHelper(nums):
            if len(nums) == 0:
                return [[]]
            ret_subsets = subsetsHelper(nums[1:])
            val = nums[0]
            res_subset = ret_subsets.copy()
            for each in ret_subsets:
                res_subset.append([val] + each.copy())
            return res_subset
        return subsetsHelper(nums)
                
