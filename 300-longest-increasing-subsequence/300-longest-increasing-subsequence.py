class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)
        return max(dp)
    
if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert s.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert s.lengthOfLIS([7,7,7,7,7,7,7]) == 1