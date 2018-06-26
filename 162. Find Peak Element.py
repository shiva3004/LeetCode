class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            middle = (start+end) // 2
            if nums[middle-1] < nums[middle] < nums[middle+1]:
                return middle
            return findPeakElement(nums[:middle])
