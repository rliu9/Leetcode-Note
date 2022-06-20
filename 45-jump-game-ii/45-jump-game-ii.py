class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_jump_max = next_jump_max = ret = 0
        for i in range(len(nums)-1):
            next_jump_max = max(next_jump_max, i+nums[i])
            if i == cur_jump_max:
                ret += 1
                cur_jump_max = next_jump_max
        return ret
    
    # O(n)
    # O(n)