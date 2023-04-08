class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = res = 0
        for right in range(1, len(prices)):
            res = max(res, prices[right]-prices[left])
            if prices[left] > prices[right]:
                left = right
        return res