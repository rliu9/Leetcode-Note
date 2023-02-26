class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = [0] * n, [0] * n
        for i in range(1, n):
            l[i] = l[i-1] + nums[i-1]
        for i in range(n-2,-1,-1):
            r[i] = r[i+1] + nums[i+1]
            
        return [abs(i-j) for i,j in zip(l,r)]