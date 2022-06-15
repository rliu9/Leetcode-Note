class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        if i == 0: return
        while nums[i-1] >= nums[i]:
            i -= 1
            if i == 0:
                nums[:] = nums[::-1]
                return
        while nums[i-1] >= nums[j]:
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[:] = nums[:i] + nums[i:][::-1]