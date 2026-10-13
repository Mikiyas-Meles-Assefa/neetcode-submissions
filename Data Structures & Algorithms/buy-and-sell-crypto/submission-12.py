class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        highest = 0
        k = 0
        while prices[k+1:] != []:
            j = prices[k+1:].index(max(prices[k+1:]))+1
            i = 0
            while i < j:
                cur = prices[k:][j]-prices[k:][i]
                if cur > highest:
                    highest = cur
                i+=1
            if i == 0:
                k+=1
            else:
                k += i
        return highest