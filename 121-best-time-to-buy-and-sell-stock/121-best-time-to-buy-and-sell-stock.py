class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding windows
        res, left = 0, 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            res = max(res, prices[right]-prices[left])
        return res
            