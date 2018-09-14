class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start + end) // 2
            if mid % 2 == 1:
                if nums[mid-1] == nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if nums[mid-1] == nums[mid]:
                    end = mid-2
                else:
                    start = mid+2
        return nums[start]
