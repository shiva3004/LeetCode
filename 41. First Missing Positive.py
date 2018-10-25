class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            if nums[0] != 1:
                return 1
            else:
                return 2
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[end] <= 0:
                end -= 1
            elif nums[start] > 0:
                start += 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        if end >= 0 and nums[end] <= 0:
            end -= 1
        # print(nums, end)
        #end = start
        if len(nums[:end + 1]) == 0:
            return 1
        max_val = max(nums[: end + 1])
        for i in range(end + 1):
            val = abs(nums[i]) - 1
            if val > end:
                continue
            if nums[val] > 0:
                nums[val] *= -1
        #     print(nums)
        # print(nums)
        for i in range(end + 1):
            if nums[i] > 0:
                return i + 1
        
        return max_val + 1

        
