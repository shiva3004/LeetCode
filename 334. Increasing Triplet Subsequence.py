class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small = float('inf'); big = float('inf')
        for n in nums:
            if n <= small:
                small = n
            elif n <= big:
                big = n
            else:
                return True
        return False
