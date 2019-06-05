class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def getPartitionIndex(left, right):
            pivot = left
            while left < right:
                if nums[left] > nums[right]:
                    nums[pivot], nums[left] = nums[left], nums[pivot]
                    pivot += 1
                left += 1
            nums[pivot],nums[right] = nums[right], nums[pivot]
            return pivot
            
        left = 0; right = len(nums) - 1
        
        while left <= right:
            partition_index = getPartitionIndex(left, right)
            if partition_index + 1 == k:
                return nums[partition_index]
            elif partition_index + 1 < k:
                left = partition_index + 1
            else:
                right = partition_index - 1
        return -1
        
