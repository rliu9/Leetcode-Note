class Solution:
    def jump(self, nums: List[int]) -> int:
        next_jump = cur = res = 0
        for i,n in enumerate(nums):
            if i == len(nums)-1:break
            next_jump = max(next_jump, i+n)
            if cur == i:
                cur = next_jump
                res += 1
        return res