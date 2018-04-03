class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_len = 100000
        res = 0
        for i in range(len(nums)-2):
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                length = abs(target - total)
                if min_len > length:
                    min_len = length
                    res = total
                if total == target:
                    return total
                elif total < target:
                    lo += 1
                else:
                    hi -= 1
        return res
