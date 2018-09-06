class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        h_map = {}
        #nums = sorted(nums)
        count = 1
        for i in range(len(nums)):
            if nums[i] in h_map:
                h_map[nums[i]] += 1
            else:
                h_map[nums[i]] = 1
        sort_keys = sorted(h_map, key=h_map.get, reverse=True)
        
        return sort_keys[:k]
            
            
        
