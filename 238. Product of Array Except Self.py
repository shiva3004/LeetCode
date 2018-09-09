class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        output = []
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]
        
        p = 1
        
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * p
            p = p*nums[i]
        
        return output
