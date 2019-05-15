class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furtherIndex = 0; lastIndex = len(nums) - 1; i = 0
        while i <= furtherIndex and furtherIndex < lastIndex:
            furtherIndex = max(furtherIndex, i + nums[i])
            i += 1
        return furtherIndex >= lastIndex
