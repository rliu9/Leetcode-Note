class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        _min = prices[0]
        for i in range(1, len(prices)):
            _min = min(_min, prices[i])
            res = max(res, prices[i] - _min)
        return res