class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_count = 0
        count = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 1
        if max_count < count:
            max_count = count
        return max_count
        
