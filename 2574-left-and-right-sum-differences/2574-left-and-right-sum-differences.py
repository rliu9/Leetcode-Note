class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = [0]*n, [0]*n
        k = nums[0]
        for i in range(1, n):
            l[i] = k
            k += nums[i]
        k = nums[-1]
        for i in range(n-2,-1,-1):
            r[i] = k
            k += nums[i]
            
        return [abs(i-j) for i,j in zip(l,r)]