class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d.keys() and d[complement] != i:
                return [d[complement], i]
            else:
                d[nums[i]] = i 
