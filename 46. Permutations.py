class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def getPerm(nums):
            if len(nums) == 1:
                return [nums]
            ret_perms = getPerm(nums[1:])
            val = nums[0]
            res_set = []
            for i in range(len(ret_perms)):
                for j in range(len(ret_perms[i])+1):
                    perm = ret_perms[i].copy()
                    perm.insert(j,val)
                    res_set.append(perm)
            return res_set
        return getPerm(nums)
