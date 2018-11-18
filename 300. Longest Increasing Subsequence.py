class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        memory = [ 1 for i in range(len(nums))]
        i = 0; j = 0
        while i < len(nums):
            j = 0
            while j < i:
                if nums[j] < nums[i]:
                    memory[i] = max(memory[j] + 1, memory[i])
                j += 1
            i += 1
        return max(memory)
