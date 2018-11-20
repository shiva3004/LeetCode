class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(nums):
            if i < len(nums) - 1 and (nums[i + 1] - nums[i]) == 1:
                end = i; start = i
                while end < len(nums):
                    if end < len(nums) -1 and nums[end+1] - nums[end] == 1:
                        end += 1
                    else:
                        res.append(str(nums[start]) + '->' + str(nums[end]))
                        break
                i = end + 1
            else:
                res.append(str(nums[i]))
                i += 1
        return res
                
