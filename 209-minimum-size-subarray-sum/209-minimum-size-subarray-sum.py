class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,size,cur_sum = 0,float('inf'),0
        for j in range(len(nums)):
            cur_sum += nums[j]
            while cur_sum >= target:
                size = min(size, j-i+1)
                cur_sum -= nums[i]
                i += 1
        return size if size!=float('inf') else 0

    # time complexity: O(n)
    # space complexity: O(1)
    
if __name__ == '__main__':
    assert 2 == Solution().minSubArrayLen(7, [2,3,1,2,4,3])
    assert 0 == Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1])
    