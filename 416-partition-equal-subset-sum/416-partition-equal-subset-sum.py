class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        half_sum = total_sum//2
        if total_sum % 2 != 0:return False
        dp = [False] * (half_sum+1)
        dp[0] = True
        for i in nums:
            for j in range(half_sum, i-1, -1):
                dp[j] = dp[j] or dp[j-i]
        return dp[-1]
    
    
    # O(n*sum)
    # O(half_sum)
