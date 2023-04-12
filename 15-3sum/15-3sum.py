class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visit, n , res= set(), len(nums), set()
        for i in range(n):
            for j in range(i+1, n):
                if -nums[i]-nums[j] in visit:
                    res.add((-nums[i]-nums[j], nums[i], nums[j]))
            visit.add(nums[i])
        return list(res)
    # time complexity: O(n^2)
    # space complexity: O(n)

if __name__ == '__main__':
    solution = Solution()
    output = sorted(solution.threeSum([-1,0,1,2,-1,-4]))
    for i,j in enumerate(sorted([[-1,-1,2],[-1,0,1]])):
        assert sorted(j) == sorted(output[i])
    assert len(output) == len([[-1,-1,2],[-1,0,1]])