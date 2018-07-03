class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        so_far = until = nums[0]
        for i in range(1,len(nums)):
            until = max(until+nums[i], nums[i])
            so_far = max(until, so_far)
        return so_far
            
