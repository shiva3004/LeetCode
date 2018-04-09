class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        print(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue
            target_3 = target - nums[i]
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                f = j + 1
                r = len(nums)-1
                while f < r:
                    if target_3 == (nums[j] + nums[f] + nums[r]):
                        res.append([nums[i], nums[j], nums[f], nums[r]])
                        while f < r and nums[f] == nums[f+1]:
                            f += 1
                        while f < r and nums[r] == nums[r-1]:
                            r -= 1
                        f += 1
                        r -= 1
                    elif (nums[j] + nums[f] + nums[r]) < target_3:
                        f += 1
                    else:
                        r -= 1
        return res
