class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = count = len(height)-1
        area = 0
        while i < j:
            if height[i] <= height[j]:
                t = count * height[i]
                i += 1
            else:
                t = count * height[j]
                j -= 1
            if t > area:
                area = t
            count -= 1
        return area
        
