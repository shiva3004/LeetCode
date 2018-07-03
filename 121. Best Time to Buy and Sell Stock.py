class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        v_max = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                s_max = max(prices[i:])
                if prices[i-1] < s_max:
                    v_max = max(s_max-prices[i-1], v_max)
        return v_max
