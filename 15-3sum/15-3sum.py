class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        res = set()
        nums.sort()
        for i,n in enumerate(nums):
            for j in range(i+1, len(nums)):
                if -nums[i]-nums[j] in hashmap:
                    res.add((-nums[i]-nums[j], nums[i], nums[j]))
            hashmap[n] = i
        return list(res)
    
    # time complexity: O(n^2)
    # space complexity: O(n)

if __name__ == '__main__':
    solution = Solution()
    output = sorted(solution.threeSum([-1,0,1,2,-1,-4]))
    for i,j in enumerate(sorted([[-1,-1,2],[-1,0,1]])):
        assert sorted(j) == sorted(output[i])
    assert len(output) == len([[-1,-1,2],[-1,0,1]])