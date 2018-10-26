class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def max(arr, val):
            res = None
            gap = 0
            for i in range(len(arr)):
                if arr[i] - val > 0:
                    if res is None or arr[i] - val < gap:
                        res = i
                        gap = arr[i] - val
            return res                       
                        
                    
        edited = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]:
                index = max(nums[i:], nums[i-1])
                nums[i - 1], nums[i + index] = nums[i + index], nums[i - 1]
                nums[i:] = sorted(nums[i:])
                edited = True
                break
        
        if not edited:
            nums[0:] = nums[::-1]
