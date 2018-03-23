class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <2:
            return -1
        l = 0
        r = sum(nums[1:])
        for i in range(len(nums)):
            if l == r:
                return i
            if i != len(nums)-1:
                l += nums[i]
                r -= nums[i+1]
        return -1
