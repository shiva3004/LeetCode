class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit = 0; i = 1
        min_val = prices[0]; max_val = prices[0]
        while i < len(prices):
            if prices[i] < max_val:
                profit += (max_val - min_val)
                min_val = prices[i]; max_val = prices[i]
            else:
                max_val = prices[i]
            i += 1
        profit += (max_val - min_val)
        return profit
