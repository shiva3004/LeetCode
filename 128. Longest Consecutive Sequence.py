class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        mapper = { 'a' : 0 }
        memory = set([])
        for num in nums:
            if num in memory:
                continue
            mapper[num] = 1
            memory.add(num)
            i = 1
            while num - i in nums and num - i not in memory:
                mapper[num] += 1
                memory.add(num-i)
                i += 1
            i = 1
            while num + i in nums and num + i not in memory:
                mapper[num] += 1
                memory.add(num+i)
                i += 1
        
        return max(mapper.values())
