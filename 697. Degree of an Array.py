class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}
        degree = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] in dictionary:
                dictionary[nums[i]].append(i)
            else:
                dictionary[nums[i]] = [i]
        for k in (dictionary.keys()):
            if degree < len(dictionary[k]):
                width = dictionary[k][-1] - dictionary[k][0]
                start = dictionary[k][0]
                end = dictionary[k][-1]
                degree = len(dictionary[k])
            elif degree == len(dictionary[k]) and width > (dictionary[k][-1] - dictionary[k][0]):
                width = dictionary[k][-1] - dictionary[k][0]
                start = dictionary[k][0]
                end = dictionary[k][-1]
        return len(nums[start:end+1])
        
        
        
        
