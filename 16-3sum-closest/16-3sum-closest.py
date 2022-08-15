class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff_target = float('inf')
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                cur = nums[i]+nums[left]+nums[right]
                if abs(cur-target) < abs(diff_target):diff_target=cur-target
                if cur < target:left+=1
                else:right-=1
                if diff_target == 0:return target
        return target+diff_target