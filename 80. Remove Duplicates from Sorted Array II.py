class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rotate_array(start, end, nums):
            temp = nums[start]
            while start < end:
                nums[start] = nums[start+1]
                start += 1
            nums[start] = temp
            
        count = 0
        j = len(nums) - 1
        i = 0
        while i < len(nums):
            if i >= j:
                break
            if nums[i] == nums[i+1]:
                count += 1
                if count == 2:
                    rotate_array(i+1, j, nums)
                    j -= 1
                    i -= 1
                    count -= 1
            else:
                count = 0
            i += 1
        return j+1
