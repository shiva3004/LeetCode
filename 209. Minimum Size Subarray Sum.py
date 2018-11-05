class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum_until = 0
        l = r = 0
        ans = [float('inf'), -1, -1]
        while r < len(nums):
            sum_until += nums[r]
            #print(sum)
            while l <= r and sum_until >= s:
                if r - l + 1 < ans[0]:
                    ans = [r - l + 1, l, r]
                sum_until -= nums[l]
                l += 1
            r += 1
        
        return 0 if ans[0] == float('inf') else ans[0]
