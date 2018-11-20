class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        mapper = self.getMappedNums(nums)
        ans = []
        for i in range(10):
            if str(i) in mapper:
                mapper[str(i)] = self.getNumberSorted(mapper[str(i)])
        if len(mapper) == 1:
            keys = mapper.keys()
            if keys[0] == '0':
                return '0'
        for key in sorted(mapper.keys(), reverse=True):
            ans.append(self.convertListToStr(mapper[key]))
        
        return ''.join(ans)
            
    
    def convertListToStr(self, arr):
        return ''.join(str(a) for a in arr)
    
    def getNumberSorted(self, arr):
        return sorted(arr, cmp = self.comparator)

    def comparator(self, a, b):
        val1 = str(a) + str(b)
        val2 = str(b) + str(a)
        if val1 <= val2:
            return 1
        else:
            return -1
 
    def getMappedNums(self, nums):
        mapper = collections.defaultdict(list)
        for num in nums:
            digit = str(num)[0]
            mapper[digit].append(num)
        return mapper
        
            
