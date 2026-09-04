class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0 
        s = 1
        mp = 0 
        
        n = len(prices)
        while s < n:
            x = prices[s] - prices[b]
            if x > mp :
                mp = x

            if prices[s] < prices[b] :
                b = s
            s += 1

        return mp
            
            
            

