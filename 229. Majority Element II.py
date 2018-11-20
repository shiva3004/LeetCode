class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        candidate1 = 0; candidate2 = 0
        count1 = 0; count2 = 0
        for val in nums:
            if candidate1 == val:
                count1 += 1
            elif candidate2 == val:
                count2 += 1
            elif count1 == 0:
                candidate1 = val
                count1 = 1
            elif count2 == 0:
                candidate2 = val
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        for candidate in set([candidate1, candidate2]):
            if self.getCount(nums, candidate) > len(nums) // 3:
                res.append(candidate)
        return res
    
    def getCount(self, nums, candidate):
        count = 0
        for val in nums:
            if val == candidate:
                count += 1
        return count
