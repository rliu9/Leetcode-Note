class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n, diff, res = len(nums), float('inf'), 0
        nums.sort()
        for i in range(n):
            left, right = i+1, n-1
            while left < right:
                cur = nums[left] + nums[i] + nums[right]
                d = abs(target-cur)
                if d == 0:return cur
                if d < diff:
                    diff = d
                    res = cur
                if cur < target:
                    left += 1
                else:
                    right -= 1
        return res