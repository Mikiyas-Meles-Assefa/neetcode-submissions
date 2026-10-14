class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        newl = []
        highestn = 0
        for i in range(len(prices)-1):
            nextn = max(prices[i+1:])
            if nextn > prices[i] and (nextn - prices[i]) > highestn:
                highestn = nextn - prices[i]
        return highestn
