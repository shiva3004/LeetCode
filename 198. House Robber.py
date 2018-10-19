class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        for i in range(len(nums) - 3, -1, -1):
            a = nums[i+2]
            b = nums[i+3] if (i + 3) < len(nums) else 0
            nums[i] += max(a, b)
        
        return max(nums[0], nums[1])
