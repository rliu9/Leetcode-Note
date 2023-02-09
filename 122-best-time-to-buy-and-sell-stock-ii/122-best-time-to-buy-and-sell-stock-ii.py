class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy
        # Collect profits as many times as possible
        
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
    
    # O(n)
    # O(1)