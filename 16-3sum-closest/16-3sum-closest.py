class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff, n, res = float('inf'), len(nums), 0
        nums.sort()
        for i in range(n):
            left, right = i+1, n-1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                d = abs(cur - target)
                if d == 0:return cur
                if d < diff:
                    diff = d
                    res = cur
                if cur < target:
                    left += 1
                else:
                    right -= 1
        return res
    
    # O(n^2)
    # O(n) -- sort
                