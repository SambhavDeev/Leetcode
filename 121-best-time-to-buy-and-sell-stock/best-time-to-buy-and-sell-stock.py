class Solution:
    def maxProfit(self, prices: List[int]) -> int:#slinding window
        maxp=0
        l,r=0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                maxp=max(maxp,(prices[r]-prices[l]))
            else:
                l=r
            r+=1
        return maxp