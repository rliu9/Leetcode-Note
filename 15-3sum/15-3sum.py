class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """visit = set()
        res = set()
        nums.sort()
        for i,n in enumerate(nums):
            for j in range(i+1, len(nums)):
                if -nums[i]-nums[j] in visit:
                    res.add((-nums[i]-nums[j], nums[i], nums[j]))
            visit.add(n)
        return list(res)"""
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:l +=1 
                elif s > 0:r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
    # time complexity: O(n^2)
    # space complexity: O(n)

if __name__ == '__main__':
    solution = Solution()
    output = sorted(solution.threeSum([-1,0,1,2,-1,-4]))
    for i,j in enumerate(sorted([[-1,-1,2],[-1,0,1]])):
        assert sorted(j) == sorted(output[i])
    assert len(output) == len([[-1,-1,2],[-1,0,1]])