class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        res,i,cur = 0,0,1
        for j in range(len(nums)):
            cur *= nums[j]
            while cur >= k:
                cur /= nums[i]
                i += 1
            res += j-i+1
        return res
    
    # time complexity: O(n)
    # space complexity: O(1)