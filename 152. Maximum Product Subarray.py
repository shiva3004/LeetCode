class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        res = nums[0]
        min_val = nums[0]
        max_val = nums[0]
        for i in range(1, len(nums)):
            prev_min_val = min_val
            min_val = min(nums[i] * min_val, nums[i] * max_val, nums[i])
            max_val = max(nums[i] * prev_min_val, nums[i] * max_val, nums[i])
            if res < max_val:
                res = max_val
        return max(res, max_val)
