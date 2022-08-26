class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for n in nums:
            if n-1 not in nums: # beginning for the consecutive sequence
                m = n+1
                while m in nums:m += 1
                res = max(res, m-n)
        return res
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)