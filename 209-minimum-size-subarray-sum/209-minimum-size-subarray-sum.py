class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,res,cur = 0, float('inf'),0
        for j in range(len(nums)):
            cur += nums[j]
            while cur >= target:
                res = min(res, j-i+1)
                cur -= nums[i]
                i += 1
        return res if res != float('inf') else 0
    
    # time complexity: O(n)
    # space complexity: O(1)
    
if __name__ == '__main__':
    assert 2 == Solution().minSubArrayLen(7, [2,3,1,2,4,3])
    assert 0 == Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1])
    