class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min, _max = prices[0], prices[0]
        res = 0
        for i in range(1, len(prices)):
            if _min > prices[i]:
                _min = prices[i]
                _max = prices[i]
            _max = max(_max, prices[i])
            res = max(res, _max-_min)
        return res