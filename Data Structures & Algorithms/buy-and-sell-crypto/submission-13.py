class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxl = [0] * n
        cur = 0
        for i in range(n - 2, -1, -1):
            cur = max(cur, prices[i + 1])
            maxl[i] = cur

        highest = 0
        for i in range(n - 1):
            highest = max(highest, maxl[i] - prices[i])
        return highest