class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pointer_0 = 0 
        pointer_1 = 0
        pointer_2 = len(nums) - 1
        
        while pointer_1 <= pointer_2:
            #print(nums, pointer_0, pointer_1, pointer_2)
            if nums[pointer_1] == 2:
                nums[pointer_1], nums[pointer_2] = nums[pointer_2], nums[pointer_1]
                pointer_2 -= 1
            elif nums[pointer_1] == 1:
                pointer_1 += 1
            elif nums[pointer_1] == 0:
                nums[pointer_0], nums[pointer_1] = nums[pointer_1], nums[pointer_0]
                pointer_1 += 1
                pointer_0 += 1
        
