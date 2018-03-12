class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        n_numbers_sum = n*(n+1)/2
        return n_numbers_sum - sum(nums)
