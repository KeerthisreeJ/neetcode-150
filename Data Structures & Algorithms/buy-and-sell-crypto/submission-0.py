class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 100
        out = 0
        for i in range(len(prices)):
            if prices[i] < m : 
                m = prices[i]

            x = prices[i] - m
            if x > out :
                out = x

        return out

        