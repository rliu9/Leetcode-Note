class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, hold = inf, 0, 0
        for p in prices:
            buy = min(buy, p - hold)
            hold = sell
            sell = max(sell, p - buy)
        return sell