class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding windows
        res, left = 0, prices[0]
        for right in prices:
            if left > right:
                left = right
            res = max(res, right-left)
        return res
            