class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def permuteUniqueHelper(nums, permutation):
            if len(nums) == 0:
                res.append(permutation)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                permuteUniqueHelper(nums[:i]+nums[i+1:], permutation+[nums[i]])
        nums = sorted(nums)
        permuteUniqueHelper(nums,[])
        return res 
